num = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    num_1 = num * i
    print(f"{num} * {i} = {num_1}")