import random

catalog = [
    {"item":101,"name": "Notebook", "category": "Paper", "price": 3.99},
    {"item":102, "name": "Pen", "category": "Writing", "price": 1.50},
    {"item":103,"name": "Pencil", "category": "Writing", "price": 0.75},
    {"item":104,"name": "Eraser", "category": "Correction", "price":
        0.99},
    {"item":105,"name": "Sharpener", "category": "Accessories", "price":
        1.25},
    {"item":106, "name": "Ruler", "category": "Measuring", "price":
        2.50},
    {"item":107, "name": "Glue Stick", "category": "Adhesive", "price":
        1.99},
    {"item":108, "name": "Scissors", "category": "Cutting", "price":
        4.99},
    {"item":109, "name": "Highlighter", "category": "Writing", "price":
        2.75},
    {"item":110, "name": "Marker", "category": "Writing", "price": 3.49},
    {"item":111, "name": "Stapler", "category": "Office Supplies",
     "price": 5.99},
    {"item":112, "name": "Staples", "category": "Office Supplies",
     "price": 1.50},
    {"item":113, "name": "Paper Clips", "category": "Office Supplies",
     "price": 2.00},
    {"item":114, "name": "Binder", "category": "Organizing", "price":
        6.50},
    {"item":115, "name": "Sticky Notes", "category": "Paper", "price":
        3.25},
    {"item":116,"name": "Index Cards", "category": "Paper", "price":
        2.99},
    {"item":117, "name": "Whiteboard Marker", "category": "Writing",
     "price": 3.75},
    {"item":118,"name": "File Folder", "category": "Organizing", "price":
        4.50},
    {"item":119,"name": "Calculator", "category": "Electronics", "price":
        12.99},
    {"item":120,"name": "Tape Dispenser", "category": "Adhesive",
     "price": 5.49}
]

def find_price(item_number):
    for product in catalog:
        if product["item"] == item_number:
            return {
                "name": product["name"],
                "category": product["category"],
                "price": product["price"],
            }
    return None

def find_extreme(category, extreme = "Highest"):
    best = None

    for product in catalog:
        if product["category"] == category:
            if best is None:
                best = product
            elif extreme == "Highest" and product["price"] > best["price"]:
                best = product
            elif extreme == "Lowest" and product["price"] < best["price"]:
                best = product
    if best is None:
        return {}
    return {best["item"]: {"name": best["name"],
                           "category": best["category"],
                           "price": best["price"]}}

def bogo_price(cart_item):
    product = find_price(cart_item["item"])
    if product is None:
        return None

    price = product["price"]
    quantity = cart_item["quantity"]

    extended = price * quantity - (quantity // 2) * price * 0.5

    return {**cart_item, "extended_price": round(extended, 2)}

# 1. random.choice: picks one random item from the catalog
def random_choice():
    item = random.choice(catalog)
    print(f"Random item: {item['name']} (${item['price']:.2f})")

# 2. random.sample: pick several different items with no repeats
def random_sample_3():
    basket = random.sample(catalog, 3)
    print("Random basket:")
    for product in basket:
        print(f"  {product['name']}: ${product['price']:.2f}")

if __name__ == "__main__":
    print(find_price(101))
    print(find_price(110))
    print(find_price(119))
    print(find_price(999))

    print(find_extreme("Paper", "Highest"))
    print(find_extreme("Paper", "Lowest"))
    print(find_extreme("Office Supplies", "Highest"))
    print(find_extreme("Office Supplies", "Lowest"))
    print(find_extreme("Nonexistent"))

    print(bogo_price({"item": 101, "quantity": 3}))
    print(bogo_price({"item": 102, "quantity": 1}))
    print(bogo_price({"item": 120, "quantity": 4}))
    print(bogo_price({"item": 999, "quantity": 2}))

    random_choice()
    random_sample_3()