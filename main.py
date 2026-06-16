from db import *

while True:

    print("\n===== ERP SYSTEM =====")
    print("1. View Customers")
    print("2. View Products")
    print("3. Sales Report")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        cursor.execute(
            "SELECT * FROM customers"
        )

        for row in cursor.fetchall():
            print(row)

    elif choice == "2":

        cursor.execute(
            "SELECT * FROM products"
        )

        for row in cursor.fetchall():
            print(row)

    elif choice == "3":

        cursor.execute(
            """
            SELECT SUM(total_amount)
            FROM orders
            """
        )

        print(
            "Sales:",
            cursor.fetchone()[0]
        )

    elif choice == "4":
        break