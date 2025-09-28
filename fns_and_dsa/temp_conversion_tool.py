CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9



def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = int(input("Enter the temperature to convert: "))
c_f = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))
if c_f == 'C' or c_f == 'c':
    result = convert_to_celsius(temperature)
    print(f"{temperature}°F is {result}°C")
elif c_f == 'F' or c_f == 'f':
    result = convert_to_fahrenheit(temperature)
    print(f"{temperature}°F is {result}°C")

else:
    print("Invalid input")

