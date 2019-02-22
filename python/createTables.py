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

createTable_USDJPY = ("CREATE TABLE USDJPY (dateTime TIMESTAMP PRIMARY KEY, open DOUBLE, close DOUBLE, high DOUBLE, low DOUBLE)")

cur.execute(createTable_USDJPY)

con.close()
