# Calculator operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by 0!")
    return a / b

# Operation functions dict
operations = {
    '1': ('Add', add),
    '2': ('Subtract', subtract),
    '3': ('Multiply', multiply),
    '4': ('Divide', divide),
    '5': ('Exit', None)
}

def calculate():
    while True:
        print("Select operation:")
        for op_code, (op_name, _) in operations.items():
            print(f"{op_code}. {op_name}")

        choice = input("Enter choice(1-5): ")
        if choice == '5':
            print("Exiting calculator...")
            break

        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue

        _, func = operations[choice]
        if func is None:
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        try:
            result = func(num1, num2)
            print(result)
        except ZeroDivisionError as e:
            print(e)

        choice = input("Do you want to perform another calculation? (y/n): ")
        if choice.lower() != 'y':
            print("Exiting calculator...")
            break

if __name__ == "__main__":
    calculate()