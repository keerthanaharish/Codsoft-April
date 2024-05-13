import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True,
                      include_digits=True, include_symbols=True):
  """
  Generates a random password based on user-specified criteria.

  Args:
      length: The desired length of the password.
      include_uppercase: Boolean flag to include uppercase letters.
      include_lowercase: Boolean flag to include lowercase letters.
      include_digits: Boolean flag to include digits.
      include_symbols: Boolean flag to include symbols.

  Returns:
      A randomly generated password string.
  """

  # Define character sets based on user choices
  char_set = ""
  if include_uppercase:
    char_set += string.ascii_uppercase
  if include_lowercase:
    char_set += string.ascii_lowercase
  if include_digits:
    char_set += string.digits
  if include_symbols:
    char_set += string.punctuation

  if not char_set:
    print("Error: Please select at least one character type.")
    return None

  # Generate random password
  password = ''.join(random.choice(char_set) for _ in range(length))
  return password

# Get user input for password length
while True:
  try:
    length = int(input("Enter desired password length (minimum 8 characters): "))
    if length < 8:
      print("Password length must be at least 8 characters.")
    else:
      break
  except ValueError:
    print("Invalid input. Please enter a number.")

# Get user input for complexity options
include_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
include_lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
include_digits = input("Include digits (y/n)? ").lower() == 'y'
include_symbols = input("Include symbols (y/n)? ").lower() == 'y'

# Generate and display password
password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
if password:
  print(f"Your generated password is: {password}")
