"""number = int(input("Please Enter any integer Value: "))
for i in range (1,number):
    if(i%2!=0):
        print("Odd Number = {0}(Skipped)".format(i))
        continue
    print("Even numbers = ",i)"""

#Python continue in While Loop Example

i = 0
while( i <= 10):
    if(i==5 or i==9):
        print("Skipped Values = ",i)
        i = i + 1
        continue
    print("The Value of the variables i is: ",i)
    i = i + 1