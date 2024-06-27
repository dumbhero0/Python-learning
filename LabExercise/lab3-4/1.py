#WAP to check the validity of email using regular expression.
import re

def is_valid_email(email):
    # Regular expression for a valid email address
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Compile the regex pattern
    pattern = re.compile(regex)
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage:
email = input("Enter the email:")
if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")