import mysql.connector
conn = mysql.connector.connect(host='localhost', password='Jalagara@60106', user='root')


if conn.is_connected():
   print("connetion established...")
