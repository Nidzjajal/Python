#Write a program in python to find out maximum and minimum number out of three user entered number.
a=float(input("Enter the First Number "))
b=float(input("Enter the  Second Number "))
c=float(input("Enter the Third Number "))
minimum=min(a,b,c)
maximum=max(a,b,c)
print(f"Minimum number : {minimum}") 
print(f"Maximum number : {maximum}")

'''
def find_max_min():
    try:
        a= float(input("Enter first number: "))
        b= float(input("Enter second number: "))
        c= float(input("Enter third number: "))

        maximum = max(a,b,c)
        minimum = min(a,b,c)

        print(f"Maximum number: {maximum}")
        print(f"Minimum number: {minimum}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    find_max_min()

'''

