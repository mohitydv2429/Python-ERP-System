from db import conn, cursor

customer_id = int(input("Customer ID: "))
product_id = int(input("Product ID: "))
qty = int(input("Quantity: "))

cursor.execute(
    "SELECT price FROM products WHERE product_id=%s",
    (product_id,)
)

price = cursor.fetchone()[0]

total = price * qty

cursor.execute(
    """
    INSERT INTO orders
    (customer_id, product_id, quantity, total_amount)
    VALUES (%s,%s,%s,%s)
    """,
    (customer_id, product_id, qty, total)
)

conn.commit()

print("Order Created")