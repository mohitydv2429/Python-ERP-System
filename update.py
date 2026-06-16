from db import conn, cursor

id = int(input("Enter Customer ID: "))
city = input("Enter New City: ")

query = """
UPDATE customers
SET city=%s
WHERE customer_id=%s
"""

cursor.execute(query, (city, id))
conn.commit()

print("Updated Successfully")