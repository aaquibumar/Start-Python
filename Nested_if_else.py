age = int(input("Please enter your age here: "))
if age <18:
    print("You are Minor")
    print("You are not Eligible to work")
else:
    if age >= 18 and age <= 60:
        print("Your are Eligible to Work")
        print("Please fill in yout details and Appy")
    else:
        print("You are too old as per government rule")
        print("Please collect your pension")