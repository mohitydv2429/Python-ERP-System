from db import cursor

cursor.execute("SELECT * FROM customers")

records = cursor.fetchall()

for row in records:
    print(row)