import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2429",
        database="erp_system"
    )

    cursor = conn.cursor()

    print("Database Connected Successfully")

except mysql.connector.Error as err:
    print("Error:", err)