#6)Write a program which will allow user to enter 10 numbers and display largest odd number from them. It will display appropriate message in case if no odd number is found.
def find_largest_odd():
    odd_numbers = []

    print("Enter 10 numbers:")
    for i in range(10):
        try:
            num = int(input(f"Enter number {i+1}: "))
            if num % 2 != 0:
                odd_numbers.append(num)
        except ValueError:
            print("Invalid input! Please enter an integer.")

    if odd_numbers:
        print(f"Largest odd number: {max(odd_numbers)}")
    else:
        print("No odd number found.")

if __name__ == "__main__":
    find_largest_odd()
