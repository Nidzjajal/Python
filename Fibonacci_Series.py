'''
Write a program in python to implement Fibonacci series up to user entered number.
(Use recursive Function)

'''

def fibonacci(n):
    if n <= 0:
        return "Enter a positive number."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter the number of terms: "))
print("Fibonacci Series:", [fibonacci(i) for i in range(1, num + 1)])
