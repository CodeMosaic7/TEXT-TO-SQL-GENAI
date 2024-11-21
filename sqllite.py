import sqlite3

# Connect to the database
connection=sqlite3.connect("student.db")

# Create a cursor object to insert records, create table
cursor=connection.cursor()

# create a table
table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
"""
cursor.execute(table_info)

# Insert Records
cursor.execute('''Insert into STUDENT values('Krish','Data Science','A')''')
cursor.execute('''Insert into STUDENT values('Dhruvi','Designing','B')''')
cursor.execute('''Insert into STUDENT values('Appoorv','Web dev','C')''')
cursor.execute('''Insert into STUDENT values('Manika','Data Science','A')''')
cursor.execute('''Insert into STUDENT values('Deepesh','Devops','D')''')

# Display All records inserted
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT;''')
for row in data:
    print(row)

# commit the changes in the database
connection.commit()
connection.close()
