# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return
def main():
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()


