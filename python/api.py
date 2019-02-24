
import requests
import createDBCon
import fxcmpy
import pandas
import createDBCon

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
    "EUR/USD":'EUR_USD',
    "GBP/USD":'GBP_USD',
    "AUD/USD":'AUD_USD',
    "USD/CAD":'USD_CAD',
    "USD/CHF":'USD_CHF',
    "NZD/USD":'NZD_USD'
}

for key, value in tradingPairs.items():
    data = con.get_candles(key, period='H1', number=5)
    #print(data.head())

    for index, row in data.iterrows():
        insert = "INSERT INTO {} (date, bidopen, bidclose, bidhigh, bidlow, askopen, askclose, askhigh, asklow) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(insert.format(value),(index.to_pydatetime(),row['bidopen'],row['bidclose'],row['bidhigh'],row['bidlow'],row['askopen'],row['askclose'],row['askhigh'],row['asklow'],))
        createDBCon.con.commit()
        break
        
createDBCon.con.close()
con.close()