
import requests
import fxcmpy
import pandas
import createDBCon
from sqlalchemy import create_engine
import psycopg2 
import io
import tokens
import constants

cur = createDBCon.con.cursor()

con = fxcmpy.fxcmpy(access_token=tokens.FXCM_API_KEY, log_level='error', server='demo')
#print(con.get_instruments())

data = pandas.DataFrame()

for key, value in constants.TRADED_PAIRS.items():
    data = con.get_candles(key, period='D1', number=3650)
    engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/postgres')
    data.head(0).to_sql(value, engine, if_exists='replace',index=True) #truncates the table, can also use append: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html

    conn = engine.raw_connection()
    curnew = conn.cursor()
    output = io.StringIO()
    data.to_csv(output, sep='\t', header=False, index=True)
    output.seek(0)
    contents = output.getvalue()
    print(value + " _ " + contents)
    curnew.copy_from(output, value, null="") # null values become ''
    conn.commit() 

conn.close() #engine connect
createDBCon.con.close() #DB connect
con.close() #API FOREX