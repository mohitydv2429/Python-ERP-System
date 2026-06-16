from tkinter import *
from db import conn, cursor

def add_customer():

    name = name_entry.get()
    phone = phone_entry.get()
    city = city_entry.get()

    query = """
    INSERT INTO customers
    (customer_name, phone, city)
    VALUES (%s,%s,%s)
    """

    cursor.execute(
        query,
        (name, phone, city)
    )

    conn.commit()

    print("Customer Added")


root = Tk()

Label(root, text="Name").grid(row=0, column=0)
Label(root, text="Phone").grid(row=1, column=0)
Label(root, text="City").grid(row=2, column=0)

name_entry = Entry(root)
phone_entry = Entry(root)
city_entry = Entry(root)

name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
city_entry.grid(row=2, column=1)

Button(
    root,
    text="Add Customer",
    command=add_customer
).grid(row=3, column=1)

root.mainloop()