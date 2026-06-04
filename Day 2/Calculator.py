print("Calculator: Available operations: +, -, *, /")
print("Type 'exit' to quit.")
while True:
    num1 = input("\nEnter first number: ").strip()
    if num1.lower() == 'exit':
        break
    
    operation = input("Enter operation (+, -, *, /): ").strip()
    if operation.lower() == 'exit':
        break

    num2 = input("Enter second number: ").strip()
    if num2.lower() == 'exit':
        break

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Error: Invalid format. Please only enter numbers.")
        continue 

    if operation == '+':
        answer = num1 + num2
        print(f"{num1} + {num2} = {answer}")
        
    elif operation == '-':
        answer = num1 - num2
        print(f"{num1} - {num2} = {answer}")
        
    elif operation == '*':
        answer = num1 * num2
        print(f"{num1} * {num2} = {answer}")
        
    elif operation == '/':
        if num2 == 0:
            print("Error: Can't divide by 0")
        else:
            answer = num1 / num2
            print(f"{num1} / {num2} = {answer}")
    else:
        print(f"Error: '{operation}' is an invalid operator.")

