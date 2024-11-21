import sqlite3
connection=sqlite3.connect("student.db")

# Create a cursor object to insert records, create table
cursor=connection.cursor()
data=cursor.execute('''Select * from STUDENT;''')
for row in data:
    print(row)

connection.commit()
connection.close()