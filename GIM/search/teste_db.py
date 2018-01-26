import psycopg2

con = psycopg2.connect(host='localhost', database='gim',
user = 'postgres', password = 'senha')
cur = con.cursor()
sql = "ALTER SEQUENCE public.core_imagens_id_seq RESTART WITH 1;"
cur.execute(sql)
sql = 'DELETE FROM public.core_imagens;'
cur.execute(sql)
con.commit()
con.close()
