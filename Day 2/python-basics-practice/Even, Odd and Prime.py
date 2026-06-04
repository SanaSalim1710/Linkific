numbers = [15, 7, 18, 17, 5, 22, 25, 13, 8, 62]

even = []
odd = []
prime = []
for number in numbers:
    if number == 2: 
        prime.append(2)

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
        # check prime
        if number > 1:
            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime.append(number)

print("Even Numbers:", even)
print("Odd Numbers:", odd)
print("Prime Numbers:", prime)

