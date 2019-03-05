import pandas as pd
import constants
from sqlalchemy import create_engine

db = constants.DATABASES['local']

engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
        user =      db['USER'],
        password =  db['PASSWORD'],
        host =      db['HOST'],
        port =      db['PORT'],
        database =  db['NAME']
    )

engine = create_engine(engine_string)

data_USDJPY = pd.read_sql_table('usd_jpy',engine)
#data_EURUSD = pd.read_sql_table('eur_usd',engine)
#data_GBPUSD = pd.read_sql_table('gbp_usd',engine)
#data_AUDUSD = pd.read_sql_table('aud_usd',engine)
#data_USDCAD = pd.read_sql_table('usd_cad',engine)
#data_USDCHF = pd.read_sql_table('usd_chf',engine)
#data_NZDUSD = pd.read_sql_table('nzd_usd',engine)

print(data_USDJPY.head())
df = pd.DataFrame
df = data_USDJPY[['date']].copy()
df['open'] =  data_USDJPY[['bidopen', 'askopen']].mean(axis=1)
df['close'] = data_USDJPY[['bidclose', 'askclose']].mean(axis=1)
df['high'] = data_USDJPY[['bidhigh', 'askhigh']].mean(axis=1)
df['low'] = data_USDJPY[['bidlow', 'asklow']].mean(axis=1)
print(df.head())

df2 = pd.DataFrame(columns=["o5","c5","h5","l5","o4","c4","h4","l4","o3","c3","h3","l3","o2","c2","h2","l2","o1","c1","h1","l1","actual_close"])
print("")
print("")
print("")
print("")
for index, row in df.iterrows():
    #s = df.index(0)
    # get the previous 5 days of data
    if index >= 5:
        df2.loc[index-5] = [
            df.loc[index-5,"open"],df.loc[index-5,"close"],df.loc[index-5,"high"],df.loc[index-5,"low"],
            df.loc[index-4,"open"],df.loc[index-4,"close"],df.loc[index-4,"high"],df.loc[index-4,"low"],
            df.loc[index-3,"open"],df.loc[index-3,"close"],df.loc[index-3,"high"],df.loc[index-3,"low"],
            df.loc[index-2,"open"],df.loc[index-2,"close"],df.loc[index-2,"high"],df.loc[index-2,"low"],
            df.loc[index-1,"open"],df.loc[index-1,"close"],df.loc[index-1,"high"],df.loc[index-1,"low"],
            df.loc[index,"close"]
        ]
    
print(df2)

    

