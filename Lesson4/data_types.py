# String Data Type

#Literal Data Type 
from pickle import FALSE


first = "Keo"
last = "Magano"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor 

pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last 
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string 

decade = str(1980)
print(type(decade))
print(decade)

statement  = "I like pop music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you ?                                                                                  

I was just checking on you.

                            All good!

'''
print(multiline)

# Escaping spacial characters 

sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good","ok"))
print(multiline)

#white space
print(len(multiline))
multiline += "                                           "
multiline = "                   "+ multiline
print(len(multiline))

#removing white space

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
print(" ")
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffin".ljust(16,".") + "$2".rjust(4))
print("Cheese Cake".ljust(16,".") + "$4".rjust(4))

print("")

#String index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

print(" ")
# Some methods that rerun Boolean data
print(first.startswith("K"))
print(first.endswith("r"))

print("")
# Boolean Data type
myvalue = False
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

print(" ")

# Numeric data types

# integer type
price = 100
best_price = int(80) 
print(type(price))
print(isinstance(best_price, int))

# FLOAT type

gpa = 3.28 
y = float(1.14)
print(type(gpa))

print(" ")

# Complex Type Used in engineering
print(" ")

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in function for number
print(" ")
print(abs(gpa))
print(round(gpa))
print(round(gpa,1))

#Math functions
import math 
print("")
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting string to number
print(" ")
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error casting incorrect data
#zip_value = int("New York")