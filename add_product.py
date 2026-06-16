from db import conn, cursor

name = input("Product Name: ")
price = float(input("Price: "))
stock = int(input("Stock: "))

query = """
INSERT INTO products
(product_name, price, stock)
VALUES (%s,%s,%s)
"""

cursor.execute(query, (name, price, stock))
conn.commit()

print("Product Added")