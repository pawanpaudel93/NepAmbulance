import psycopg2
conn = psycopg2.connect("host='localhost' dbname='nepambulance' user='pawan' password='pawan33'")
curs = conn.cursor()
curs.execute(open('province.sql', 'r').read())
conn.commit()
curs.execute(open('district.sql', 'r').read())
conn.commit()
curs.close()
conn.close()