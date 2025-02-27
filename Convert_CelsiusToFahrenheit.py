#Write a Python Program to Convert Celsius to Fahrenheit and vice –a-versa.
print("Menu:\n 1 -> Convert Celsius to Fahrenheit \n 2 -> Convert Fahrenheit to Celsius\n")

# Taking user input
a = int(input("Enter your choice (1 or 2): "))

if a == 1:
    b = float(input("Enter the temperature in Celsius: "))
    print("Fahrenheit =", (b * 1.8) + 32)

elif a == 2:
    c = float(input("Enter the temperature in Fahrenheit: "))
    print("Celsius =", (c - 32) / 1.8)  # Fixed formula

else:
    print("Invalid choice! Please enter 1 or 2.")
