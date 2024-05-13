def calculate(num1, num2, operator):
  """
  Performs the calculation based on the provided operator.

  Args:
      num1: The first number.
      num2: The second number.
      operator: The arithmetic operator (+, -, *, /).

  Returns:
      The result of the calculation.
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero is not allowed.")
      return None  # Indicate error
    else:
      return num1 / num2
  else:
    print("Invalid operator. Please use +, -, *, or /.")
    return None  # Indicate error

while True:
  # Get user input
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose an operator (+, -, *, /): ")
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    continue

  # Perform calculation and display result
  result = calculate(num1, num2, operator)
  if result is not None:
    print(f"{num1} {operator} {num2} = {result}")

  # Ask if user wants to continue
  choice = input("Do you want to perform another calculation? (y/n): ")
  if choice.lower() != 'y':
    break

print("Thank you for using the calculator!")
