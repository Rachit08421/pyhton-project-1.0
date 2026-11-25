# Simple Calculator Project
# Concepts: functions, exception handling, list, loops

history = []   # to store old calculations


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b


def menu():
    print()
    print("---- CALCULATOR ----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Show history")
    print("7. Exit")


while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "7":
        print("Thank you!")
        break

    elif choice == "6":
        if len(history) == 0:
            print("No history yet")
        else:
            for h in history:
                print(h)

    elif choice in ["1", "2", "3", "4", "5"]:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == "1":
                result = add(x, y)
                sign = "+"
            elif choice == "2":
                result = subtract(x, y)
                sign = "-"
            elif choice == "3":
                result = multiply(x, y)
                sign = "*"
            elif choice == "4":
                result = divide(x, y)
                sign = "/"
            else:
                result = modulus(x, y)
                sign = "%"

            print("Answer =", result)
            history.append(str(x) + " " + sign + " " + str(y) + " = " + str(result))

        except ValueError:
            print("Please enter numbers only!")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        finally:
            print("Done")

    else:
        print("Wrong choice, try again")
