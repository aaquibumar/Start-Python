"""total = 0
num = int(input("Please Enter the Integer Below 10: "))
while(num <= 10):
    total = total + num
    num = num + 1
print("Total is: ",total)"""

#While Loop with Else Statement


total = 0
num = int(input("Please Enter the Integer Below 100: "))
while(num< 100):
    total = total + num
    num = num + 1
    print("Total is: ",total)
else:
    print("Your Value is Greater than 100")
