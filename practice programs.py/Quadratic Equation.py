#import complex math module
import cmath
#take input from user a, b and c print the taken input
a = int(input("Enter first no:"))
print("First entered no is: ", a)
b = int(input("Enter second no:"))
print("Second entered no is:",b)
c = int(input("Enter third no:"))
print("Third entered no is:",c)

d = (b**2) - (4*a*c)
print("Value of discriminant",d)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The soutions are {0} and {1}".format(sol1,sol2))