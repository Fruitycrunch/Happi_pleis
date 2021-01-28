import psycopg2
from flask import Flask

con = psycopg2.connect(
            host = "localhost",
            port = 5432,
            database = "memphisdb",
            user = "postgres",
            password = "admin"
)

cur = con.cursor()

cur.execute("insert into employees (id,name) values (%s,%s)", (7,'coco'))
cur.execute( "select id, name from employees" )


rows = cur.fetchall()

for r in rows:
    print(f"id: {r[0]} name: {r[1]}")

con.commit()
cur.close()
con.close()

