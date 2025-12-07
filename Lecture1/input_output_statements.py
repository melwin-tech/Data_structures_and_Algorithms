
# How to take input from user and print function in python

# 1. Taking Input From User

# Python takes user input using input().
# It always returns a string, unless you typecast it.
# Example:
name = input("Enter your name: ")
print("Hello", name)

# 2. print() Function + Attributes

# print() has useful arguments:
'''
Attribute	            Meaning
sep	                    Separator between values (default: space " ")
end	                    What to print at the end (default: newline "\n")
file	                Where to print (default: console)
flush	                Force write (default: False)
'''
# Examples:
print("A", "B", "C", sep="-")  # Output: A-B-C
print("Hello", end=" ")        # End with space instead of newline
print("World")                 # Output: Hello World

# 3. Typecasting (Converting Data Types)

# Since input() returns a string, you convert using:

'''
Function	Converts to
int()	    integer
float() 	decimal number
str()	    string
bool()	    boolean
'''
# Examples:
age = int(input("Enter your age: "))   # convert to integer
height = float(input("Enter height: ")) # convert to float

print("Age:", age)
print(type(age))
print("Height:", height)
print(type(height))