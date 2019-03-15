from tensorflow.keras.callbacks import TensorBoard
import tensorflow as tf
from keras.layers import Dropout, Activation 
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import constants
from sklearn.preprocessing import normalize
import datetime
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from sklearn.preprocessing import StandardScaler

db = constants.DATABASES['local']
engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
    user =      db['USER'],
    password =  db['PASSWORD'],
    host =      db['HOST'],
    port =      db['PORT'],
    database =  db['NAME']
)
def predictWithData(transformedDataSet, curr_Pair):
    model = tf.keras.models.load_model('model_predictFutureCandle')  
    transformedDataSet = np.array(transformedDataSet)
    transformedDataSet = scaler.transform(transformedDataSet)
    print(transformedDataSet)
    prediction = model.predict([transformedDataSet])
    prediction = pd.DataFrame(data=prediction)
    
    return prediction.to_json(orient='records')
    #modelname="model_predictFutureCandle"

def prepareData(curr_Pair):
    #pull in the data and format it by taking the mean between the asking and bid price
    engine = create_engine(engine_string)
    data = pd.read_sql_table(curr_Pair, engine) #TODO change table name to a var
    df = pd.DataFrame
    df = data[['date']].copy()
    df['open'] =  data[['bidopen', 'askopen']].mean(axis=1)
    df['close'] = data[['bidclose', 'askclose']].mean(axis=1)
    df['high'] = data[['bidhigh', 'askhigh']].mean(axis=1)
    df['low'] = data[['bidlow', 'asklow']].mean(axis=1)

    transformedDataSet = pd.DataFrame(columns=["o5","c5","h5","l5","o4","c4","h4","l4","o3","c3","h3","l3","o2","c2","h2","l2","o1","c1","h1","l1"])

    #convert the data frame into data sets for training and testing
    for index, row in df.iterrows():
        if index == 5:
            transformedDataSet.loc[index-5] = [
                df.loc[index-5,"open"],df.loc[index-5,"close"],df.loc[index-5,"high"],df.loc[index-5,"low"],
                df.loc[index-4,"open"],df.loc[index-4,"close"],df.loc[index-4,"high"],df.loc[index-4,"low"],
                df.loc[index-3,"open"],df.loc[index-3,"close"],df.loc[index-3,"high"],df.loc[index-3,"low"],
                df.loc[index-2,"open"],df.loc[index-2,"close"],df.loc[index-2,"high"],df.loc[index-2,"low"],
                df.loc[index-1,"open"],df.loc[index-1,"close"],df.loc[index-1,"high"],df.loc[index-1,"low"]
            ]         
            
            break
    # transformedDataSet = transformedDataSet.reset_index(drop=True)
    # transformedDataSet = transformedDataSet.values        

    return predictWithData(transformedDataSet, curr_Pair)

prepareData("usd_jpy")