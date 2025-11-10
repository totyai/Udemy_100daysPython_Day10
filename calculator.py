"""
This project would perform a basic operation on 2 numbers.
It would also continue the calculation wiht the result if needed.
OR start everything from sratch
"""

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# TODO - Write fucntions for the basic operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dict as the values. Keys = "+", "-", "*", "/"
# Storing funcitons into variables uses the same name of the fucniton but without the () - not to call it
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide, 
}

# TODO - Use the dict operations to perform the calculations. Multiple 4 * 8
# print(operations["*"](4,8))

# TODO - Program asks the user to type the first number
first_num = input("What's the first number?: ")

# TODO - Program asks the user to type a mathematical operator
operation = input("+ \n - \n * \n / \n Pick an operation: ")

# TODO - Program asks the user to type the second number
second_number = input("What's the next number?: ")

# TODO - Program works out the result based on chosen math operator
if operation == "+":
    result = operations["+"](first_num, second_number)
elif operation == "-":
    result = operations["-"](first_num, second_number)
elif operation == "*":
    result = operations["*"](first_num, second_number)
elif operation == "/":
    result = operations["/"](first_num, second_number)
else:
    print("Invalid operation. Try again.")

print(f"{first_num} {operation} {second_number} = {result}")

# TODO - Program asks if the user wantes to continue wokring with previous result
cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

# TODO - If yes, program loops to use the previous result as the first number and then repreats the calc process

# TODO - If no, program asks the user for the first number again and wipes all memory of previous run