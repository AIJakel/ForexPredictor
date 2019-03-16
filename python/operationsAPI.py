import requests
import pandas as pd
from sqlalchemy import create_engine
import constants
import predictWithTransform

db = constants.DATABASES['local']
engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
    user =      db['USER'],
    password =  db['PASSWORD'],
    host =      db['HOST'],
    port =      db['PORT'],
    database =  db['NAME']
)

def getAllHistorical(curr_Pair):
    engine = create_engine(engine_string)
    data = pd.read_sql_table(curr_Pair, engine) #TODO change table name to a var
    df = pd.DataFrame
    df = data[['date']].copy()
    df['open'] =  data[['bidopen', 'askopen']].mean(axis=1)
    df['close'] = data[['bidclose', 'askclose']].mean(axis=1)
    df['high'] = data[['bidhigh', 'askhigh']].mean(axis=1)
    df['low'] = data[['bidlow', 'asklow']].mean(axis=1)

    return df.to_json(orient='records')

def getPredictionData(curr_Pair):
    return predictWithTransform.prepareData(curr_Pair)