from db import conn, cursor

name = input("Enter Name: ")
phone = input("Enter Phone: ")
city = input("Enter City: ")

query = """
INSERT INTO customers
(customer_name, phone, city)
VALUES (%s,%s,%s)
"""

cursor.execute(query, (name, phone, city))
conn.commit()

print("Customer Added Successfully")