def calculator():
    while True:
        print("\nWelcome to CLI Calculator")
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")
        print("5 - Exit")    
        option = input("Choose an operation (1-5): ").strip()

        if option == "5":
            print("Exiting the calculator. Goodbye!")
            break

        if option in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: ").strip())
                num2 = float(input("Enter second number: ").strip())
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if option == "1":
                result = num1 + num2
                print(f"The result of addition is: {result}")
            elif option == "2":
                result = num1 - num2
                print(f"The result of subtraction is: {result}")
            elif option == "3":
                result = num1 * num2
                print(f"The result of multiplication is: {result}")
            elif option == "4":
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of division is: {result}")
                else:
                    print("Error: Division by zero is not allowed.")
        else:
            print("Invalid option entered. Please choose between 1 and 5.")

if __name__ == "__main__":
    calculator()
# calculator.py 
