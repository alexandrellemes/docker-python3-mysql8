# https://qiita.com/shoma/items/59c9c907e8f217ab7b14

import dataset
import mysql.connector

db = dataset.connect('mysql://root:123456@mysqldb/sample')

table = db['Alchemist']

table.insert(dict(name='Alphonse Elric'))
table.insert_many([dict(name='Edward Elric', titled='Fullmetal'), dict(name='Roy Mustang', titled='Flame')])


print('List table...')
db=mysql.connector.connect(host="mysqldb", user="root", password="123456",database="sample")

cursor=db.cursor()

cursor.execute("SELECT * FROM sample.Alchemist")

for campos in cursor:
    print(campos)

cursor.execute("SELECT * FROM sample.Alchemist")
myresult = cursor.fetchone()

print(myresult)