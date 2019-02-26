
import requests
import fxcmpy
import pandas
from sqlalchemy import create_engine
import psycopg2 
import io
import createDBCon

db = createDBCon.DATABASES['local']

#FXCMPY API key
api_KEY_FX = '7de7723acba2f89e1d875750e7e93be13180646a'

con = fxcmpy.fxcmpy(access_token=api_KEY_FX, log_level='error', server='demo')
#print(con.get_instruments())

data = pandas.DataFrame()
tradingPairs = {
    "USD/JPY":'usd_jpy',
    "EUR/USD":'eur_usd',
    "GBP/USD":'gbp_usd',
    "AUD/USD":'aud_usd',
    "USD/CAD":'usd_cad',
    "USD/CHF":'usd_chf',
    "NZD/USD":'nzd_usd'
}

for key, value in tradingPairs.items():
    data = con.get_candles(key, period='D1', number=3650)

    engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
        user = db['USER'],
        password = db['PASSWORD'],
        host = db['HOST'],
        port = db['PORT'],
        database = db['NAME']
    )

    engine = create_engine(engine_string)
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
con.close() #API FOREX