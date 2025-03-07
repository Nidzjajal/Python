'''
    10) Write a Python program to perform following operation on given string input:
    a) Count Number of Vowel in given string
    b) Count Length of string (do not use Len ())
    c) Reverse string
    d) Find and replace operation
    e) check whether string entered is a palindrome or not
'''
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    return count

def string_length(string):
    count = 0
    for _ in string:
        count += 1
    return count

def reverse_string(string):
    return string[::-1]

def find_and_replace(string, find_word, replace_word):
    return string.replace(find_word, replace_word)

def is_palindrome(string):
    return string == string[::-1]

# Taking user input
string = input("Enter a string: ")

# Performing operations
print(f"Number of vowels: {count_vowels(string)}")
print(f"Length of string (without len()): {string_length(string)}")
print(f"Reversed string: {reverse_string(string)}")

# Find and replace operation
find_word = input("Enter word to find: ")
replace_word = input("Enter word to replace with: ")
print(f"Modified string: {find_and_replace(string, find_word, replace_word)}")

# Palindrome check
if is_palindrome(string):
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
