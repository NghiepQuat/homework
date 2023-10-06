import pyodbc

conn = pyodbc.connect(' DRIVER={SQL Server};SERVER=.\SQLEXPRESS;DATABASE=QLMonAn;Trusted_Connection=yes;')


cursor = conn.cursor()
cursor.execute("SELECT @@version")
db_version = cursor.fetchone()
conn.close()
print("Ban dang dung he quan tri CSDL SQL server phien ban", db_version)

