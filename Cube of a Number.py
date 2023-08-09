#Python Program to calculate cube of a Number
"""num = float(input("Please Enter a number:"))
cube = num*num*num
print("The Cube of a Given Number {0} = {1}".format(num,cube))"""

"""num = float(input("Enter a number:"))
cube = num ** 3
print("Cube is {0} = {1}".format(num,cube))"""

#python program to find  cube of a Number using Functions

def cube(number):
    return number * number * number
number = float(input("Please Enter any numeric Value:"))

cub = cube(number)

print("The cude of a Given Number {0} = {1}".format(number,cub))