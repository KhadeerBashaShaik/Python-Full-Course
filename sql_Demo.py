import mysql.connector

conn=mysql.connector.connect(user='root',password='Khajavali12@',host='127.0.0.1')

cursor=conn.cursor()

cursor.execute("DROP database IF exists MyDataBase")

sql="create database demo0";

cursor.execute(sql)

print("List  of databases : ")
cursor.execute("show databases")
print(cursor.fetchall())
conn.close()