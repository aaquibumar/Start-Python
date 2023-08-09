number = int(input("Please Enter any integer below 100: "))
for i in range (0,100):
    if number == i:
        print("User entered value is within the range (Below 100)")
        break
else:
    print("User entered value is outside the range (Above 100)")