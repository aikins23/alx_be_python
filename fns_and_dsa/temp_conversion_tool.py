CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temperature = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

c_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if c_f.lower() == 'c':
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {result:.2f}°F")
elif c_f.lower() == 'f':
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result:.2f}°C")
else:
    print("Invalid input")
