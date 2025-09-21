num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The result of {num_1} + {num_2} = {num_1 + num_2}")
    case "-":
        print(f"The result of {num_1} - {num_2} = {num_1 - num_2}")
    case "*":
        print(f"The result of {num_1} * {num_2} = {num_1 * num_2}")
    case "/":
        if num_2 ==0:
            print(f"Cannot divide by zero.")
        else:
            print(f"The result of {num_1} / {num_2} = {num_1 / num_2}")