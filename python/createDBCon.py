import psycopg2

#connect to DB local
con = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "password",
    port = "5432")

cur = con.cursor()