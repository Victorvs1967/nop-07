from server import db


db.create_all()

# import psycopg2

# def readDB():
#     conn = psycopg2.connect(
#     host='localhost', port='5432', database='DataCollector',
#     user='victors', password='victor77')
#     cur = conn.cursor()
#     cur.execute('select * from data')
#     rows = cur.fetchall()
#     conn.close()

#     return rows

# [print(x) for x in readDB()]
