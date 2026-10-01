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
            print(f"{product['name']}, {product['category']}: ${product['price']}")
            return product["price"]

    print("Item not found.")
    return None

def find_extreme(category, extreme):
    best = None
    for product in catalog:
        if product["category"] == category:
            if best is None:
                best = product
            elif extreme == "highest" and product["price"] > best["price"]:
                best = product
            elif extreme == "lowest" and product["price"] < best["price"]:
                best = product
    print(f"{best['name']}, {best['category']} : ${best['price']:.2f}")

def bogo_price(cart_item):
    price = next(p["price"] for p in catalog if p["item"] == cart_item["item"])
    quantity = cart_item["quantity"]

    extended = price * quantity - (quantity // 2) * price * 0.5

    return {**cart_item, "extended_price": round(extended, 2)}

if __name__ == "__main__":
    find_price(119)
    find_extreme("Paper", "highest")