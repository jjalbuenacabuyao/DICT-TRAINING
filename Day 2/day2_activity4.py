temperature = float(input("Enter the temperature: "))

unit = input("Fahrenheit or Celsius: ").lower()

if unit == "c":
    converted_temperature = (temperature * 9 / 5) + 32
    print(f"{temperature} degree Celsius is {converted_temperature} degree Fahrenheit")
elif unit == "f":
    converted_temperature = (temperature - 32) * (5 / 9)
    print(f"{temperature} degree Fahrenheit is {converted_temperature} degree Celcius")
else:
    print("Invalid input, enter c for Celsius or f for Fahrenheit.")