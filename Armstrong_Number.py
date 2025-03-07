#7)	Write a Python program to check if the number provided by the user is an Armstrong number.
num = int(input("Enter a number: "))  
total = 0  
digits = len(str(num))  # Count the number of digits  

# Take each digit, raise it to the power of 'digits', and add to total
for digit in str(num):  
    total += int(digit) ** digits  

# Check if the total matches the original number
if total == num:  
    print(f"{num} is an Armstrong number.")  
else:  
    print(f"{num} is not an Armstrong number.")  

'''
num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) ** len(str(num)) for digit in str(num))

if num == sum_of_digits:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
'''
