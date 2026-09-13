item_amount = int(input("Enter the length of list of items: "))
total = 0.0
value = 0

while value < item_amount:
    item_name = input("Enter item name: ")
    quantity = int(input("Enter the quantity of items: "))
    unit_price = float(input("Enter unit price: "))

    extended_price = unit_price * quantity
    total += extended_price

    print(f"{item_name}, ${unit_price:.2f}, {quantity}, ${extended_price:.2f}")

    value += 1

print("Total extended price = $" + f"{total:.2f}")

