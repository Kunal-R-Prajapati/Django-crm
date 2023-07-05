# Run this only one time

# Install Mysql on your computer
# Installing the required packages to establih the connection
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '********' # Enter your mysql server password here
)   

# prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE Name_of_Database")
 


print("ALL Done")