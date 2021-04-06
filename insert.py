import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='tiger',database='pythontest')
cur=mydb.cursor()
s="INSERT INTO Book(bookid,title,price) VALUES(%s,%s,%s)"
b1=(1,'python',340)
cur.execute(s,b1)
mydb.commit()