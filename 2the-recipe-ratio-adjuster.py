"""Task 1: Start
Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.

Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

Task 2: Quantity Calculation
Calculate the adjustment factor by dividing the desired servings by the original servings.

Use a try block to catch any arithmetic errors that may occur during the calculation.

Task 3: Serving Success
If the calculation is successful, display the adjusted recipe quantities to the user.

Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation."""


def recipe_adjuster():

    original_servings = int(input("Please enter the original number of servings: " ))
    desired_servings = int(input("Please enter the desired number of servings: " ))

    try:
        adjustment_factor = desired_servings / original_servings
        print(f"The adjustment factor is {adjustment_factor:.2f}")
    except ZeroDivisionError:
        print("Can not divide by zero")
    except ValueError:
        print("Please enter a valid number")
    except ArithmeticError as a:
        print(f"Error: {a} check your equations.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print(f"Thank you for using this calculator! Enjoy your cooking!")
    

while True:
    welcome = input("Hello there! Do you need help with some calculation? yes/no: ").lower().strip()
    if welcome != "yes":
        break
    else:
        recipe_adjuster()