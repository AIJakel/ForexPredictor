import psycopg2

#connect to DB local
con = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "password",
    port = "5432")

#connect to DB Heroku
# con2 = psycopg2.connect(
#     host = "ec2-54-83-196-179.compute-1.amazonaws.com",
#     database = "d7h0bl2kg6v3c2",
#     user = "nqfromejvqdewm",
#     password = "d4268ae3afeffc9507eb9537d7ce4c53a82e4a0578a1f16b41ea4d489bad4686",
#     port = "5432",
#     URI = "postgres://nqfromejvqdewm:d4268ae3afeffc9507eb9537d7ce4c53a82e4a0578a1f16b41ea4d489bad4686@ec2-54-83-196-179.compute-1.amazonaws.com:5432/d7h0bl2kg6v3c2",
#     CLI = "heroku pg:psql postgresql-horizontal-37622 --app forexpredictor")

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
