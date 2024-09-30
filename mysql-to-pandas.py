import pandas as pd
import mysql.connector

#Making connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydb"
)

#Checking the connection to mysql db.
if conn.is_connected():
    print("Connected bro!!")
else:
    print("Not Connected bro!")

# Getting data into a Pandas DataFrame
query = "SELECT * FROM sales_data"
df = pd.read_sql(query, conn)

# Close connection
conn.close()

# View data
print(df.head())
