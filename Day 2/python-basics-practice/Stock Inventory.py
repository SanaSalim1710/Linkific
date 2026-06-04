inventory = {
    "Shirt": 0,
    "Dress": 20,
    "Jeans": 8
}

for item, stock in inventory.items():
    if 0 < stock < 10:
        print(item, ": Low Stock")
    elif stock > 10 :
        print(item, ": Available")
    else: 
        print(item, ": Out of stock")

        