
import requests
import fxcmpy
import pandas
import createDBCon
from sqlalchemy import create_engine
import psycopg2 
import io

cur = createDBCon.con.cursor()
#currency layer API key
api_KEY_CL = 'ecdfab01b625c4f4316c0de2ed0f83ff'

#7-day live rates API key _ 2019/03/02
api_KEY_LR = 'f8a3aea1be'

#1Forge API key
api_KEY_1F = 'WCEkhBqODkTgMKh2c1rpmdX22e6PIG5C'

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
    data = con.get_candles(key, period='H1', number=10)
    #print(data.head())
    """    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "password",
    port = "5432")"""

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

    """for index, row in data.iterrows():
        insert = "INSERT INTO {} (date, bidopen, bidclose, bidhigh, bidlow, askopen, askclose, askhigh, asklow) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(insert.format(value),(index.to_pydatetime(),row['bidopen'],row['bidclose'],row['bidhigh'],row['bidlow'],row['askopen'],row['askclose'],row['askhigh'],row['asklow'],))
        createDBCon.con.commit()
        break
    """    

conn.close() #engine connect
createDBCon.con.close() #DB connect
con.close() #API FOREX