#Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal
Decimal =int(input("Enter the decimal :"))

binary=bin(Decimal)
octal=oct(Decimal)
hexadecimal=hex(Decimal)

print(f"Binary: {binary[2:]}")        # Removing '0b' prefix
print(f"Octal: {octal[2:]}")          # Removing '0o' prefix
print(f"Hexadecimal: {hexadecimal[2:].upper()}")# Removing '0x' prefix & converting to uppercase

'''

print(binary)     #0b1001110000
print(octal)       #0o1160
print(hexadecimal)  #0x270

'''
