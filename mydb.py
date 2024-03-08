# Install Mysql on computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# or .. pip install msql-connector-python
# MT@10x7yt
import mysql.connector

database = mysql.connector.connect(host="localhost", user="root", passwd="MT@10x7yt")

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All done!")
