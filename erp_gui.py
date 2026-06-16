import tkinter as tk

root = tk.Tk()
root.title("ERP Management System")
root.geometry("800x500")

title = tk.Label(
    root,
    text="ERP Management System",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

btn_customer = tk.Button(
    root,
    text="Customer Management",
    width=25,
    height=2
)
btn_customer.pack(pady=10)

btn_product = tk.Button(
    root,
    text="Product Management",
    width=25,
    height=2
)
btn_product.pack(pady=10)

btn_order = tk.Button(
    root,
    text="Order Management",
    width=25,
    height=2
)
btn_order.pack(pady=10)

btn_report = tk.Button(
    root,
    text="Sales Reports",
    width=25,
    height=2
)
btn_report.pack(pady=10)

root.mainloop()