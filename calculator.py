def simple_calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    operation = input("Enter the number corresponding to the operation (1, 2, 3, 4): ")
    
    if operation == '1':
        result = num1 + num2
        operation_name = "Addition"
    elif operation == '2':
        result = num1 - num2
        operation_name = "Subtraction"
    elif operation == '3':
        result = num1 * num2
        operation_name = "Multiplication"
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            operation_name = "Division"
        else:
            result = "undefined (cannot divide by zero)"
            operation_name = "Division"
    else:
        result = "Invalid operation"
        operation_name = "None"
    
    print(f"Operation: {operation_name}")
    print(f"Result: {result}")

# Run the calculator
simple_calculator()
