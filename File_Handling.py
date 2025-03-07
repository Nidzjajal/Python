'''
Write a program in Python to implement readline, readlines, write line and writelines
file handling mechanisms.
'''

# Writing to a file
file = open("example.txt", "w")
file.write("Hello, this is the first line.\n")  # Writing a single line
file.writelines(["Second line.\n", "Third line.\n"])  # Writing multiple lines
file.close()

print("File written successfully!")

# Reading the file
file = open("example.txt", "r")

print("\nReading first line using readline():")
print(file.readline())  # Reads only the first line

print("\nReading all lines using readlines():")
print(file.readlines())  # Reads all lines as a list

file.close()
