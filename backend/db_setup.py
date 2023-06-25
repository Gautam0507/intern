import mysql.connector 

database = mysql.connector.connect(
    host= 'localhost', 
    user = 'root',
    passwd = 'sqlpass'
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE Meter")
print("all done!")