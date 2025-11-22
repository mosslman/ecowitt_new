import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mojo2*"
)
mycursor = db.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS pythondb")
mycursor.execute("USE pythondb")
mycursor.execute("CREATE TABLE IF NOT EXISTS pytable (name VARCHAR(255), address VARCHAR(255))")

for tb in mycursor:
    print(tb)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
sqlQuery = "INSERT INTO pytable (name, address) VALUES (%s, %s)"    
student1 = ("John", "Highway 21")
mycursor.execute(sqlQuery, student1)
db.commit()
print(mycursor.rowcount, "record inserted.")
student1 = ("Sandy", "Longfold")
mycursor.execute(sqlQuery, student1)
db.commit()
mycursor.execute("SELECT * FROM pytable")
for x in mycursor:
    print(x)

students = [
    ('Peter', 'Lowstreet 4'),  
    ('Amy', 'Apple st 652'),  
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633') ]

mycursor.executemany(sqlQuery, students)
db.commit()
print(mycursor.rowcount, "record inserted.")
sql = "SELECT * FROM pytable where name=%s"
mycursor.execute(sql, ('Sandy', ))

#for x in mycursor:
#    print(x)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)

sql="DROP TABLE IF EXISTS pytable"
mycursor.execute(sql)
db.commit()

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)


db.close()
