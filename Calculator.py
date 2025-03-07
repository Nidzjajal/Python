#Write a program to make a simple calculator (using functions).
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

def calculator():
    last_result = None
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Exponentiate")
        print("7. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7): ")
        
        if choice == '7':
            confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
            if confirm in ('yes', 'y'):
                print("Exiting calculator. Goodbye!")
                break
            else:
                continue
        
        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    last_result = add(num1, num2)
                    print(f"Result: {last_result}")
                elif choice == '2':
                    last_result = subtract(num1, num2)
                    print(f"Result: {last_result}")
                elif choice == '3':
                    last_result = multiply(num1, num2)
                    print(f"Result: {last_result}")
                elif choice == '4':
                    last_result = divide(num1, num2)
                    print(f"Result: {last_result}")
                elif choice == '5':
                    last_result = modulus(num1, num2)
                    print(f"Result: {last_result}")
                elif choice == '6':
                    last_result = exponentiate(num1, num2)
                    print(f"Result: {last_result}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()
