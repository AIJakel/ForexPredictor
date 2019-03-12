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
#data_EURUSD = pd.read_sql_table('eur_usd',engine)
#data_GBPUSD = pd.read_sql_table('gbp_usd',engine)
#data_AUDUSD = pd.read_sql_table('aud_usd',engine)
#data_USDCAD = pd.read_sql_table('usd_cad',engine)
#data_USDCHF = pd.read_sql_table('usd_chf',engine)
#data_NZDUSD = pd.read_sql_table('nzd_usd',engine)

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

msk = np.random.rand(len(transformedDataSet_USDJPY)) < 0.8
x_train_USDJPY = transformedDataSet_USDJPY[msk]
x_test_USDJPY = transformedDataSet_USDJPY[~msk]

y_train_USDJPY = x_train_USDJPY[["actual_open","actual_close","actual_high","actual_low"]].reset_index(drop=True)
#y_train_USDJPY = y_train_USDJPY[["actual_open"]]
y_test_USDJPY = x_test_USDJPY[["actual_open","actual_close","actual_high","actual_low"]].reset_index(drop=True)
#y_test_USDJPY = y_test_USDJPY [["actual_open"]]
x_train_USDJPY = x_train_USDJPY[["o5","c5","h5","l5","o4","c4","h4","l4","o3","c3","h3","l3","o2","c2","h2","l2","o1","c1","h1","l1"]].reset_index(drop=True)
x_test_USDJPY =x_test_USDJPY[["o5","c5","h5","l5","o4","c4","h4","l4","o3","c3","h3","l3","o2","c2","h2","l2","o1","c1","h1","l1"]].reset_index(drop=True)

# scaler = StandardScaler()
# scaler.fit(x_train_USDJPY)
x_pred2 = y_test_USDJPY
x_train_USDJPY = x_train_USDJPY.values
x_test_USDJPY = x_test_USDJPY.values
# x_train_USDJPY = scaler.transform(x_train_USDJPY)
# x_test_USDJPY = scaler.transform(x_test_USDJPY)

# scaler.fit(y_train_USDJPY)
y_train_USDJPY = y_train_USDJPY.values
y_test_USDJPY = y_test_USDJPY.values
# y_train_USDJPY = scaler.transform(y_train_USDJPY)
# y_test_USDJPY = scaler.transform(y_test_USDJPY)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(4, activation=tf.nn.relu))

model.compile(optimizer='adam',
                loss='mean_squared_error',
                metrics =['accuracy'])

model.fit(x_train_USDJPY, y_train_USDJPY, epochs=10)

val_loss, val_acc = model.evaluate(x_test_USDJPY, y_test_USDJPY)
print(val_loss, val_acc)

prediction = model.predict(x_test_USDJPY,verbose=1)
#dataset = pd.DataFrame({'Column1':prediction[:,0],'Column2':prediction[:,1]})
prediction = pd.DataFrame(data=prediction)
#print(prediction.head())


with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(prediction)
    print()
    print()
    print()
    print()
    print()
    print()
    print(x_pred2)


prediction.plot()
plt.show()

x_pred2.plot()
plt.show()


# fig, ax = plt.subplots()
# ax2 = ax.twinx()

# prediction.plot(ax=ax)
# x_pred2.plot(ax=ax2, ls="--")

# plt.show()