from db import cursor

cursor.execute(
    """
    SELECT SUM(total_amount)
    FROM orders
    """
)

sales = cursor.fetchone()[0]

print("Total Sales =", sales)