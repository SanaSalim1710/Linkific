pin_num = "1234"
attempts_left = 3
while attempts_left > 0:
    pin_entry = input("Enter your 4 digit PIN number: ")
    if pin_entry == pin_num:
        print("Access granted.")
        break  
    attempts_left -= 1
    print(f"Incorrect PIN. You have {attempts_left} attempts left.\n")
if attempts_left == 0:
    print("Your account has been locked for exceeding maximum attempts.")

    