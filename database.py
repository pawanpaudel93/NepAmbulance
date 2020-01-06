import psycopg2
from decouple import config
conn = psycopg2.connect(config('DATABASE_URL'))
# conn = psycopg2.connect("dbname='nepambulance' user='pawan' password='pawan33'")
curs = conn.cursor()
# curs.execute(open('province.sql', 'r').read())
# conn.commit() // add province manually
curs.execute(open('district.sql', 'r').read())
conn.commit()
curs.close()