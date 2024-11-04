# Michael Cook
# UWYO COSC 1010
# Submission Date 11/01/24
# Lab 08
# Lab Section: 16
# Sources, people worked with, help given to: Google Gemini (2024/04/11) to explain the instructions of the requirements in part III
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def string_user(input_string):
  try:
    int_userinput = int(input_string)
    return int_userinput
  except ValueError:
    try:
      float_userinput = float(input_string)
      formate_float = f"{float_userinput:.1f}"
      return formate_float
    except ValueError:
      return False

while True:
  strings = input("enter a string to see if its an int or float: ")
  if strings.lower() == "exit":
    break
  result = string_user(strings)
  if result is not False:
    print(result)
  else:
    print("Input is not a float or a string")


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, lower_bound, upper_bound):
  """solve for y = mx + b"""
  if lower_bound > upper_bound:
    return False
  x_value = range(lower_bound, upper_bound + 1)
  y_value = []
  for x in x_value:
    y = m * x + b
    y_value.append(y)
  return y_value

while True:
    m = input("enter m: ")
    if m.lower() == "exit":
        break
    b = input("enter b: ")
    if b.lower() == "exit":
        break
    lower_bound = input("enter lower bound: ")
    if lower_bound.lower() == "exit":
        break
    upper_bound = input("enter upper bound: ")
    if upper_bound.lower() == "exit":
        break
    
    try:
        m, b = float(m), float(b)
        lower_bound, upper_bound = int(lower_bound), int(upper_bound)
        
        y_values = slope_intercept(m, b, lower_bound, upper_bound)
        print(y_values)  # Print the results
        
    except ValueError:
        print("Invalid input. Please enter numbers.")


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
# x = (-b ± √(b² - 4ac)) / (2a)
def solve_quadratic(a, b, c):
  """Solve the quadratic equation"""
  discriminant = b**2 - 4*a*c
  if discriminant < 0:
    return "null"
  else:  
    def my_sqrt(n):
      if n < 0:
        return "null"
      if n == 0:
        return 0
      x = n 
      y = (x + 1) // 2
      while y < x:
        x = y
        y = (x + n // x) // 2
      return x

    solving_quad = my_sqrt(discriminant)
    if solving_quad == "null":
      return "null"
    x1 = (-b + solving_quad)/(2*a)
    x2 = (-b - solving_quad)/(2*a)

  return x1, x2

while True:
  a = input("enter a: ")
  if a.lower() == "exit":
    break
  b = input("enter b: ")
  if b.lower() == "exit":
    break
  c = input("enter c: ")
  if c.lower() == "exit":
    break
  try:
    a,b,c = int(a), int(b), int(c)
    roots = solve_quadratic(a,b,c)
    if roots == "null":
      print("null")

    elif type(roots) == tuple:
      print("Roots: ", roots[0], roots[1])

  except ValueError:
    print("Invalid input. Please enter integer values for a, b, and c.")