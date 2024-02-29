import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'

)

#prepare cursorObject
cursorObject = dataBase.cursor()

#create Db
cursorObject.execute("CREATE DATABASE elderco")

print ("All Done")