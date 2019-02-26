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

