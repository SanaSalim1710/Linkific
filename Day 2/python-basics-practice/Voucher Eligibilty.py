def free_shipping(is_member,has_voucher, area):
    if is_member and has_voucher:
        if area == "West Malaysia" or area == "East Malaysia":
            print("Free shipping voucher applied to your order")
        else:
            print("Sorry, your location is not eligible for free shipping.")
    else:
        print("Sorry, you need to be a member and have a voucher for free shipping")

free_shipping(True,True,"West Malaysia")
free_shipping(False, True, "West Malaysia")
free_shipping(True, True, "International")
