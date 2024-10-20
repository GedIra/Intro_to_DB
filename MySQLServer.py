import mysql.connector

#Connecting to the Database

mydb = mysql.connector.connect(
      host = 'localhost',
      user = 'Ged',
      password = 'Mypassword'
)

mycursor = mydb.cursor()

#Executions

try:
  mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

except Exception as e:
  print(e)

else:
  print("Database 'alx_book_store' created successfully!")

finally:
  mydb.close
  mycursor.close



