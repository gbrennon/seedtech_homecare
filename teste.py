import sqlite3

conn = sqlite3.connect('homecare')
c = conn.cursor()
c.execute("SELECT * FROM exame ORDER BY id DESC LIMIT 1") 
a = c.fetchall()
#conn.commit()
#for query in query:
print a[0][0]

