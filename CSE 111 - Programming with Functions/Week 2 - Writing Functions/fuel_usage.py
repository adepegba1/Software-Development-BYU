"""
Write a Python program named fuel_usage.py that asks the user
for three numbers:
1. A starting odometer value in miles
2. An ending odometer value in miles
3. A amount of fuel in gallons

Your program must calculate and print fuel efficiency in both
miles per gallon and liters per 100 kilometers. Your program
must have three functions named as follows:
1. main
2. miles_per_gallon
3. lp100k_from_mpg

All user input and printing must be in the main function. In other
words, the miles_per_gallon and lp100k_from_mpg functions must not
call the the input or print functions.
"""
def main():
  # Get an odometer value in U.S. miles from the user.
  start = float(input("Enter the first odometer reading (miles): "))
  # Get another odometer value in U.S. miles from the user.
  end = float(input("Enter the second odometer reading (miles): "))
  # Get a fuel amount in U.S. gallons from the user.
  amount = float(input("Enter the amount of fuel used (gallons): "))
  # Call the miles_per_gallon function and store
  mpg = miles_per_gallon(start, end, amount)
  # the result in a variable named mpg.
  print(f"{mpg:.2f} miles per gallon")
  # Call the lp100k_from_mpg function to convert the
  # miles per gallon to liters per 100 kilometers and
  # store the result in a variable named lp100k.
  lp100k = lp100k_from_mpg(mpg)
  # Display the results for the user to see.
  print(f"{lp100k:.2f} liters per 100 kilometer")
  pass
def miles_per_gallon(start_miles, end_miles, amount_gallons):
  """Compute and return the average number of miles
  that a vehicle traveled per gallon of fuel.
  Parameters
  start_miles: An odometer value in miles.
  end_miles: Another odometer value in miles.
  amount_gallons: A fuel amount in U.S. gallons.
  Return: Fuel efficiency in miles per gallon.
  """
  mpg = abs(end_miles - start_miles) / amount_gallons
  return mpg
def lp100k_from_mpg(mpg):
  """Convert miles per gallon to liters per 100
  kilometers and return the converted value.
  Parameter mpg: A value in miles per gallon
  Return: The converted value in liters per 100km.
  """
  lp100k = 235.215 / mpg
  return lp100k
# Call the main function so that
# this program will start executing.
main()