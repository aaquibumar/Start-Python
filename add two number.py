#a=10
#b=99
#sum=a+b
#print(sum)
#print(a+b)
#print(10+99)

#add Two numbers With User Input

#number1 = input("Please enter the first number:")
#number2 = input("Please enter the second number:")
#using airthmatic + Operator
#sum = int(number1) + float(number2)
#print('The sum of {0} and {1} is {2}'.format(number1, number2,sum))

#number1 = float(input("Please Enter the First:"))
#number2 = float(input("Please Enter the second:"))

#using airthmatic + operator
#sum = number1+ number2
#print('The sum of {0} and {1} is {2}'.format(number1,number2,sum))

#add two numbers using functions

#def addNumbers(a,b):
 #   return a + b
#a = float(input("Enter the First Value ="))
#b = float(input("Enter the Second Value ="))

#result = addNumbers(a,b)
#print(result)

#add two numbers without using Operator

#a = float(input("Enter the First Value = "))
#b = float(input("Enter the Second Value = "))

#numList = [a,b]
#result = sum(numList)
#print(result)

#nums = input("Enter Two Numbers Seperated by Space = ")

#numList =[float(n)for n in nums.split()]

#result = sum(numList)
#print(result)

#two numbers in Python using for loop
#result = 0

#for i in range(5):
    #n = float(input("Enter a Value ="))
    #result += n
    #print(result)

#Addition of two numbers in Python using While loop

#result = 0
#i = 0

#while i<2:
    #n = float(input("Enter a Value ="))
    #result += n
    #i += 1

#print(result)

#Python Program to Add Two Numbers using Lambda Function

#result = lambda a,b: a + b

#print(result(30.5,40))

#The below example code accepts the two numbers and uses the lambda function to perform addition.

#x = float(input("Enter the First Value = "))
#y = float (input ("Enter the second Value = "))

#result = lambda a,b : a + b
#print(result(x,y))

#use of lambda and reduce functions.

from functools import reduce

nums = input ("Enter two Number Seperated by Space = ")
numList = [float(n) for n in nums.split()]

result = reduce(lambda a,b : a+b, numList)

print(result)


