# temp_conversion_tool.py
# Objective: Demonstrate variable scope using global conversion factors
# for temperature conversion between Celsius and Fahrenheit.

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    Formula: (F - 32) * (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    Formula: (C * (9/5)) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


if __name__ == "__main__":
    try:
        # Prompt user for temperature
        temp_input = input("Enter the temperature to convert: ")
        
        # Validate numeric input
        temperature = float(temp_input)  # raises ValueError if not numeric
        
        # Prompt user for unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature:.1f}°F is {converted}°C")
        elif unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature:.1f}°C is {converted}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    
    except ValueError as e:
        print("Invalid temperature. Please enter a numeric value.")