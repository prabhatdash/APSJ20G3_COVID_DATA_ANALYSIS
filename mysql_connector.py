import mysql.connector
dbc=mysql.connector.connect(host="localhost",user="root",passwd="macintosh",database="covid")
cursor=dbc.cursor()
