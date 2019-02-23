import psycopg2

#connect to DB
con = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "password",
    port = "5432")

#cursor
cur = con.cursor()
createTable_USDJPY = ("CREATE TABLE USDJPY (dateTime timestamp without time zone, open numeric NOT NULL, close numeric NOT NULL, high numeric NOT NULL, low numeric NOT NULL, PRIMARY KEY (dateTime))")
createTable_EURUSD = ("CREATE TABLE EURUSD (dateTime timestamp without time zone, open numeric NOT NULL, close numeric NOT NULL, high numeric NOT NULL, low numeric NOT NULL, PRIMARY KEY (dateTime))")
createTable_GBPUSD = ("CREATE TABLE GBPUSD (dateTime timestamp without time zone, open numeric NOT NULL, close numeric NOT NULL, high numeric NOT NULL, low numeric NOT NULL, PRIMARY KEY (dateTime))")
createTable_AUDUSD = ("CREATE TABLE AUDUSD (dateTime timestamp without time zone, open numeric NOT NULL, close numeric NOT NULL, high numeric NOT NULL, low numeric NOT NULL, PRIMARY KEY (dateTime))")
createTable_USDCAD = ("CREATE TABLE USDCAD (dateTime timestamp without time zone, open numeric NOT NULL, close numeric NOT NULL, high numeric NOT NULL, low numeric NOT NULL, PRIMARY KEY (dateTime))")
createTable_USDCHF = ("CREATE TABLE USDCHF (dateTime timestamp without time zone, open numeric NOT NULL, close numeric NOT NULL, high numeric NOT NULL, low numeric NOT NULL, PRIMARY KEY (dateTime))")
createTable_NZDUSD = ("CREATE TABLE NZDUSD (dateTime timestamp without time zone, open numeric NOT NULL, close numeric NOT NULL, high numeric NOT NULL, low numeric NOT NULL, PRIMARY KEY (dateTime))")

try:
    cur.execute(createTable_USDJPY)
except:
    ...
try:    
    cur.execute(createTable_EURUSD)
except:
    ...
try: 
    cur.execute(createTable_GBPUSD)
except:
    ...
try: 
    cur.execute(createTable_AUDUSD)
except:
    ...
try: 
    cur.execute(createTable_USDCAD)
except:
    ...
try: 
    cur.execute(createTable_USDCHF)
except:
    ...
try: 
    cur.execute(createTable_NZDUSD)
except:
    ...

con.commit()
con.close()
