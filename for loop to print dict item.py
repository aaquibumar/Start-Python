dd = {1:'apple',2:'banana',3:'orange',4:'kiwi'}

#for loop iterates and print keys
for val in dd:
    print(val)

#for loop iterate and print the values inside it
for val in dd:
    print(dd[val])

#for loop to iterate and print the values inside it
for val in dd:
    print(val,"Key Value = ", dd[val])

for i in dd.values():
    print(i)