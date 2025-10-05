def safe_divide(numerator, denominator):
    try:
        result = int(numerator) / int(denominator)
        print(f"The result of {numerator} / {denominator} is {result}")
    except ZeroDivisionError:
        print(f"Hello your numerator {numerator} is Zero and is invalid")
    except ValueError:
        print(f"The result of {numerator} is not a valid number")
