# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def modulus_op(a, b):
    if b == 0:
        return None
    return int(a) % int(b)


def exponent(base, power):
    return base ** power


def show_menu():
    print("\n================================")
    print("        SIMPLE CALCULATOR")
    print("================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    running = True

    while running:
        show_menu()
        choice_input = input("Select an operation (1-7): ")

        if not choice_input.isdigit():
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        choice = int(choice_input)

        if choice == 7:
            print("Goodbye!")
            running = False
            continue

        if choice < 1 or choice > 7:
            print("Invalid choice. Please enter a number between 1 and 7.")
            continue

        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))

        result = None
        symbol = " "

        if choice == 1:
            result = add(num1, num2)
            symbol = "+"
        elif choice == 2:
            result = subtract(num1, num2)
            symbol = "-"
        elif choice == 3:
            result = multiply(num1, num2)
            symbol = "*"
        elif choice == 4:
            result = divide(num1, num2)
            symbol = "/"
        elif choice == 5:
            result = modulus_op(num1, num2)
            symbol = "%"
        elif choice == 6:
            result = exponent(num1, num2)
            symbol = "^"

        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result: {num1:.2f} {symbol} {num2:.2f} = {result:.2f}")


if __name__ == "__main__":
    main()
