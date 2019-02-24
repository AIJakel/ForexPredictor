
import requests
import createDBCon
import fxcmpy
import pandas

#currency layer API key
api_KEY_CL = 'ecdfab01b625c4f4316c0de2ed0f83ff'

#7-day live rates API key _ 2019/03/02
api_KEY_LR = 'f8a3aea1be'

#1Forge API key
api_KEY_1F = 'WCEkhBqODkTgMKh2c1rpmdX22e6PIG5C'

#FXCMPY API key
api_KEY_FX = '7de7723acba2f89e1d875750e7e93be13180646a'

'''
resp = requests.get('http://live-rates.com/api/price?key='+api_KEY_LR+'&rate=USD_JPY,EUR_USD,GBP_USD,AUD_USD,USD_CAD,USD_CHF,NZD_USD')
if resp.status_code == 200:
    for items in resp.json():
        print(items['currency'])
     #   insert = ("INSERT INTO {} VALUES ({},{},{},{},{},{},{})".format(items['currency'],items['open']items['close'],items['high'],items['low'],items['bid'],items['ask']))
    #createDBCon.cur.execute(insert)
'''
con = fxcmpy.fxcmpy(access_token=api_KEY_FX, log_level='error', server='demo')
#print(con.get_instruments())

data = pandas.DataFrame()
tradingPairs = {
    "USD/JPY":"USD_JPY",
    "EUR/USD":"EUR_USD",
    "GBP/USD":"GBP_USD",
    "AUD/USD":"AUD_USD",
    "USD/CAD":"USD_CAD",
    "USD/CHF":"USD_CHF",
    "NZD/USD":"NZD_USD"
}
for pair in tradingPairs:
    data = con.get_candles(pair.key, period='H1', number=5)
    print(data.head())
    insert = ()
    createDBCon.cur.execute(insert)



con.close()





createDBCon.con.close