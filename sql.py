import sqlite3

#connect to sqlite
connection=sqlite3.connect("student.db")

#create a cursor object to insert record,create table,retrive results etc
cursor=connection.cursor()

#create table
table_info="""
Create  table STUDENT(NAME VARCHAR(24),CLASS VARCHAR(24),SECTION VARCHAR(24),MARKS INT)
"""
cursor.execute(table_info)

#insert some records
cursor.execute('''INSERT INTO STUDENT VALUES ('Sravan', 'Data Science', 'A',45)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Amal', 'Data Science', 'B',65)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Aman', 'Devops', 'C',62)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Ajay', 'Data Science', 'C',98)''') 

#display the records
print("Inserted Records are")

data=cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

#close the connection
connection.commit()
connection.close()

