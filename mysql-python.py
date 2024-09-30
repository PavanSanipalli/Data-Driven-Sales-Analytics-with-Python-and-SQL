import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb"
)

cursor = conn.cursor()

# Fetch data
cursor.execute("SELECT * FROM superstore_dataset")
result = cursor.fetchall()

for row in result:
    print(row)

# Close the connection
conn.close()
