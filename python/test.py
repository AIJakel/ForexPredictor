import pandas as pd
import constants
from sqlalchemy import create_engine
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

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

df_USDJPY = pd.DataFrame
df_USDJPY = data_USDJPY[['date']].copy()
df_USDJPY['open'] =  data_USDJPY[['bidopen', 'askopen']].mean(axis=1)
df_USDJPY['close'] = data_USDJPY[['bidclose', 'askclose']].mean(axis=1)
df_USDJPY['high'] = data_USDJPY[['bidhigh', 'askhigh']].mean(axis=1)
df_USDJPY['low'] = data_USDJPY[['bidlow', 'asklow']].mean(axis=1)

transformedDataSet_USDJPY = pd.DataFrame(columns=["o5","c5","h5","l5","o4","c4","h4","l4","o3","c3","h3","l3","o2","c2","h2","l2","o1","c1","h1","l1","actual_open","actual_close","actual_high","actual_low"])

for index, row in df_USDJPY.iterrows():
    #s = df.index(0)
    # get the previous 5 days of data
    if index >= 5:
        transformedDataSet_USDJPY.loc[index-5] = [
            df_USDJPY.loc[index-5,"open"],df_USDJPY.loc[index-5,"close"],df_USDJPY.loc[index-5,"high"],df_USDJPY.loc[index-5,"low"],
            df_USDJPY.loc[index-4,"open"],df_USDJPY.loc[index-4,"close"],df_USDJPY.loc[index-4,"high"],df_USDJPY.loc[index-4,"low"],
            df_USDJPY.loc[index-3,"open"],df_USDJPY.loc[index-3,"close"],df_USDJPY.loc[index-3,"high"],df_USDJPY.loc[index-3,"low"],
            df_USDJPY.loc[index-2,"open"],df_USDJPY.loc[index-2,"close"],df_USDJPY.loc[index-2,"high"],df_USDJPY.loc[index-2,"low"],
            df_USDJPY.loc[index-1,"open"],df_USDJPY.loc[index-1,"close"],df_USDJPY.loc[index-1,"high"],df_USDJPY.loc[index-1,"low"],
            df_USDJPY.loc[index,"open"],df_USDJPY.loc[index,"close"],df_USDJPY.loc[index,"high"],df_USDJPY.loc[index,"low"]
        ]