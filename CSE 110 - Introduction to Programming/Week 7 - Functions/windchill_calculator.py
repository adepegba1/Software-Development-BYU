"""
Your assignment is to write a program that asks the user for a temperature and 
then shows the wind chill values for various wind speeds at that temperature.

Your program should compute and display the wind chill for wind speeds of 5, 10, 15, ..., 60 miles per hour,
just like the National Weather Service chart does. To help users who are more familiar with Celsius,
your program should allow temperature to be entered in either Celsius or Fahrenheit, 
and if needed, convert the Celsius temperature to Fahrenheit before using the formula.
If the user enter different temperature, the program will inform them that they enter the wrong command.
"""
def temperature_conversion(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit

def windchill_calculator(temperature, speed):
    result = 35.74 + (0.6215 * temperature) - 35.75 * pow(speed, 0.16) + (0.4275 * temperature) * pow(speed, 0.16)
    return result

user_input_temperature = float(input("What is the temperature? "))
temperature_value = input("Fahrenheit or Celsius (F/C)? ")
temperature_value = temperature_value.upper()

if temperature_value == "F" or temperature_value == "C":
    for speed in range(5, 65, 5):
        if temperature_value == "F":
            windchill_answer = windchill_calculator(user_input_temperature, speed)
            print(f"At temperature {user_input_temperature:.1f}F, and wind speed {speed} mph, the windchill_answer is: {windchill_answer:.2f}F")
        
        elif temperature_value == "C":
            convert = temperature_conversion(user_input_temperature)
            windchill_answer = windchill_calculator(convert, speed)
            print(f"At temperature {convert:.1f}F, and wind speed {speed} mph, the windchill_answer is: {windchill_answer:.2f}F")
    
else:
    print("Invalid temperature selected!!!")
   

