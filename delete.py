from db import conn, cursor

id = int(input("Enter Customer ID: "))

query = """
DELETE FROM customers
WHERE customer_id=%s
"""

cursor.execute(query, (id,))
conn.commit()

print("Deleted Successfully")