def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        print(f"The result of the division is {result}")
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")
    except ValueError:
        print(f"Error: Please enter numeric values only.")
