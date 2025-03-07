'''
Write a program in python to implement Factorial series up to user entered number.
(Use recursive Function)
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

num = int(input("Enter a number: "))

print("Factorial Series:")
for i in range(num + 1):
    print(f"{i}! = {factorial(i)}")
