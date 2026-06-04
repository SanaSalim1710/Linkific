menu = {
    "Fries": 13,
    "Pizza": 20,
    "Ketchup": 8
}

total = 0
ongoing = True
while ongoing == True:
    item = input('Order item or reply "complete" if you are done: ')
    if item.lower() == "complete":
        ongoing = False
    elif item.title() in menu:
        total = total + menu[item.title()]
    else:
        print("Sorry, the item is not on the menu")
print("Total cost:", total)
    
