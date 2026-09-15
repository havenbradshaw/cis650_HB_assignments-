sales_records = [
    "Laptop Pro 15 ",
    "Wireless Mouse",
    "Keyboard Mechanical",
    "USB C Hub ",
    "Monitor 27inch ",
    "Webcam HD",
    "Headphones noise cancel"]

prices = [1299.99, 45.50, 89.00, 35.99, 349.00, 79.99,
          159.00]

data = dict(zip(sales_records, prices))  # zip + dict drops duplicates automatically

print("Cleaned Sales Report")
print("--------------------")
for name in sorted(data):
    print(f"{name} : ${data[name]:,.2f}")