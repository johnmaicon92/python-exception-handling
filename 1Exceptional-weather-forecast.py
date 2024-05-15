"""
Task 1: Start
Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be converted to a number.

Task 2: Temperature Conversion
Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

Task 3: User Experience
Implement an else block that prints the converted temperature in a user-friendly format.

Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
"""

def fahrenheit_to_celsius():
    fahrenheit = int(input("Please enter the temperature in Fahrenheit: "))

    try:
        celsius = (fahrenheit - 32) * 5/9
        print(f"The temperature in Celsius is {celsius:.1f}")

    except ZeroDivisionError:
        print("Can not divide by zero")

    except OverflowError:
        print("Overflow error")

    except ValueError:
        print("Something went wrong. Please enter a valid number.")

    else:
        print(f"{fahrenheit}° Fahrenheit is equal to {celsius:.1f}° Celsius!")

    finally:
            print("Thank you for using the weather forecast application!")

    return celsius
   


def celsius_to_fahrenheit():
    celsius = int(input("Please enter the temperature in Celsius: "))

    try:
        fahrenheit = (celsius * 9/5) + 32
        print(f"The temperature in Fahrenheit is {fahrenheit:.1f}")

    except ZeroDivisionError:
        print("Can not divide by zero")

    except OverflowError:
        print("Overflow error")

    except ValueError:
        print("Something went wrong. Please enter a valid number.")

    else:
        print(f"{celsius}° Celsius is equal to {fahrenheit:.1f}° Fahrenheit!")

    finally:
            print("Thank you for using the weather forecast application!")

    return fahrenheit
   


while True:
    welcome = input("Hello there! The Temperature you want to convert is in Celsius or Fahrenheit? (C)/(F): ").upper().strip()
    if welcome == "C":
        celsius_to_fahrenheit()
    elif welcome == "F":
     fahrenheit_to_celsius()
    break