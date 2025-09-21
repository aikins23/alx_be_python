number = int(input("Enter the size of the pattern: "))
row = 0
while row < number:
    for col in range(1, number):
        print("*", end="")
    print()
    row += 1

