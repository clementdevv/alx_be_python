FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    while True:
        user_input = input("Enter the temperature value to convert (input 'q' to quit): ").strip().lower()
        
        if user_input == 'q':
            print("Goodbye!")
            break        
        try:
            temp_value = float(user_input)
            temp_unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')

            if temp_unit == 'F':
                temp_f = float(temp_value)
                converted_temp = convert_to_celsius(temp_f)
                print(f"{temp_f}F is {converted_temp:.2f}C")
            elif temp_unit == 'C':
                temp_c = float(temp_value)
                converted_temp = convert_to_fahrenheit(temp_c)
                print(f"{temp_c}C is {converted_temp:.2f}F")
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                continue

                break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
        
if __name__ == "__main__":
    main()