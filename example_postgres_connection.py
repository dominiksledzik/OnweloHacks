import psycopg2

conn = psycopg2.connect(
    port="5433",
    host="localhost",
    database="postgres",
    user="abcd",
    password="1234")

cur = conn.cursor()
print('PostgreSQL database version:')
cur.execute('SELECT version()')

db_version = cur.fetchall()
print(db_version)

cur.close()