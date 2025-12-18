def get_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid number. Try again!")


num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

try:
    res = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Division result is:", res)
finally:
    print("Execution done. Thanks!")