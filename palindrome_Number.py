#Write a Python program to check if the number provided by the user is a palindrome ornot.
num = input("Enter a number: ")  

if num == num[::-1]:  # Reverse the number and check if it's the same
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
