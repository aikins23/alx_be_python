number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    num_1 = number * i
    print(f"{number} * {i} = {num_1}")