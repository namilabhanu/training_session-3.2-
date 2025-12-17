try:
    pass
except Exception:
    pass


try:
    a = int(input("enter a number: "))
    b = int(input("enter another number: "))
    result = a / b
    print("The result is:", result)

except ZeroDivisionError:
    print("Error: you cannot divide by zero.")
except ValueError:
    print("Error: invalid input. Please enter numeric values.")

print("Execution continues...")


# Catching Multiple Exceptions
try:
    x = int(input("Enter number: "))
    y = 10 / x
except (ZeroDivisionError, ValueError):
    print("Error occurred")


# Else Block
# Runs only when no exception occurs.
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Oops!")
else:
    print("You entered:", num)


# Finally Block
try:
    file = open("data.txt")
    read_data = file.read()
    print(read_data)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed!")


# Raising Custom Exceptions
age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("Age must be at least 18!")