def temperature_converter():

    print("Temperature Conversion Selected!")
    print('''Select conversion:

    1. Celsius to Fahrenheit
    2. Fahrenheit to Celsius
    3. Celsius to Kelvin
    4. Kelvin to Celsius''')

    temp = int(input("please choose"))

    if temp == 1 :
        degree = float(input("Enter temperature: "))
        fahrenheit = (degree * 9/5) + 32
        print(f"Celsius to Fahrenheit: {fahrenheit}")
    
    elif temp == 2 :
        degree = float(input("Enter temperature: "))
        celsius = (degree - 32) * (5/9)
        print(f"Fahrenheit to Celsius: {celsius}")
    
    elif temp == 3 :
        degree = float(input("Enter temperature: "))
        kelvin = degree + 273.15
        print(f"Celsius to Kelvin: {kelvin}")

    elif temp == 4:
        degree = float(input("Enter temperature: "))
        celsius = degree - 273.15
        print(f"Kelvin to Celsius: {celsius}")

    else:
        print("Invalid choice!")

def weight_converter():

    print("Weight Conversion selected.")
    print(''' WEIGHT CONVERSION 

    1. Kilogram to Gram
    2. Gram to Kilogram
    3. Kilogram to Pound
    4. Pound to Kilogram

    Please choose:''')

    weight_choice = int(input("Please choose: "))

    if weight_choice == 1:
        weight = float (input("please enter your weight: "))
        gram = weight * 1000
        print(f"Kilogram to Gram: {gram}")
    
    elif weight_choice == 2:
        weight = float (input("please enter your weight: "))
        kilogram = weight / 1000
        print(f"Gram to Kilogram: {kilogram}")

    elif weight_choice == 3:
        weight = float (input("please enter your weight: "))
        pound = weight * 2.20462
        print(f"Kilogram to Pound: {pound}")

    elif weight_choice == 4:
        weight = float (input("please enter your weight: "))
        kilogram = weight / 2.20462
        print(f"Pound to Kilogram: {kilogram}")

    else:
        print("Invalid choice!")

def length_converter():

    print("Length Conversion Selected!")

    print(''' LENGTH CONVERSION 

    1. Meter to Centimeter
    2. Centimeter to Meter
    3. Kilometer to Meter
    4. Meter to Kilometer

    Please choose:''')

    length_choice = int(input("Please choose: "))

    if length_choice == 1:
        length = float(input("Please enter length: "))
        centimeter = length * 100
        print(f"Meter to Centimeter: {centimeter}")

    elif length_choice == 2:
        length = float(input("Please enter length: "))
        meter = length / 100
        print(f"Centimeter to Meter: {meter}")

    elif length_choice == 3:
        length = float(input("Please enter length: "))
        meter = length * 1000
        print(f"Kilometer to Meter: {meter}")

    elif length_choice == 4:
        length = float(input("Please enter length: "))
        kilometer = length / 1000
        print(f"Meter to Kilometer: {kilometer}")

    else:
        print("Invalid choice!")


#main
while True:
    print(''' UNIT CONVERTER 

    1. Temperature Conversion
    2. Weight Conversion
    3. Length Conversion
    0. Exit

    Please select an option:''')

    user = int(input("please enter a number: "))

    if user == 1 :
        temperature_converter()

    elif user == 2:
        weight_converter()

    elif user == 3:
        length_converter()

    elif user == 0:
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
