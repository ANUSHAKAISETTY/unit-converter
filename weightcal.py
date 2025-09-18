def length_converter():
    print("\nLength Conversion")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    choice = int(input("Choose conversion: "))
    
    if choice == 1:
        meters = float(input("Enter value in meters: "))
        print(f"{meters} meters = {meters / 1000} kilometers")
    elif choice == 2:
        km = float(input("Enter value in kilometers: "))
        print(f"{km} kilometers = {km * 1000} meters")
    else:
        print("Invalid choice!")


def weight_converter():
    print("\nWeight Conversion")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    choice = int(input("Choose conversion: "))
    
    if choice == 1:
        kg = float(input("Enter value in kilograms: "))
        print(f"{kg} kilograms = {kg * 1000} grams")
    elif choice == 2:
        g = float(input("Enter value in grams: "))
        print(f"{g} grams = {g / 1000} kilograms")
    else:
        print("Invalid choice!")


def temperature_converter():
    print("\nTemperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Choose conversion: "))
    
    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c} °C = {(c * 9/5) + 32} °F")
    elif choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f} °F = {(f - 32) * 5/9:.2f} °C")
    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            length_converter()
        elif choice == 2:
            weight_converter()
        elif choice == 3:
            temperature_converter()
        elif choice == 4:
            print("Exiting Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
