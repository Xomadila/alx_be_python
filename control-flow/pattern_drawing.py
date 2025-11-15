# pattern_drawing.py
# Objective: Draw a square pattern of asterisks using while and nested for loops.

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for rows
while row < size:
    # For loop for columns
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to next line after each row
    row += 1