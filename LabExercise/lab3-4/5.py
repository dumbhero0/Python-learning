# WAP to handle divide by zero and invalid array index exceptions using try..except...finally blocks.

try:
      # Example 1: Handling ZeroDivisionError
      num1 = 10
      num2 = 0
      result = num1 / num2  # Attempting division by zero
      print(f"Result of division: {result}")  # This line won't execute due to exception

except ZeroDivisionError:
      print("Error: Division by zero is not allowed.")

finally:
      print("Example 1 execution complete.\n")

try:
      # Example 2: Handling IndexError
      my_list = [1, 2, 3]
      index = 5
      element = my_list[index]  # Attempting to access index that is out of range
      print(f"Element at index {index}: {element}")  # This line won't execute due to exception

except IndexError:
      print(f"Error: Index {index} is out of range for the list.")

finally:
      print("Example 2 execution complete.")
