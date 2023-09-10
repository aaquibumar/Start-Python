"""stri ='aaquib'

for x in stri:
    print(x,end = '')

stng = 'aaquibumar'

for x in stng:
    print(x,end = '')

print("\n***Output***")
itr = iter(stng)
print(next(itr))

sting = 'umaraaquib'
for x in sting:
    print(x,end = '')
print("\n****Example****")
itr = iter(sting)

print(next(itr))
print(next (itr))
print(next (itr))
print(next (itr))
print(next (itr))
print(next (itr))
print(next (itr))
print(next (itr))
print(next (itr))
print(next (itr))

#Python List iterator

numbers = [10,20,30,40,50]

itr = iter(numbers)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

#Python Set Iterator Example

mySet = {1,2,3,4,5}

ittr = iter(mySet)

print(ittr.__next__())
print(ittr.__next__())
print(ittr.__next__())
print(ittr.__next__())
print(ittr.__next__())

#Tuple Example

fruits = ('Apple','Orange','Grape','Banana','Kiwi')

fruit_itr = iter(fruits)

print(next(fruit_itr))
print(next(fruit_itr))
print(next(fruit_itr))
print(next(fruit_itr))
print(next(fruit_itr))"""

#Create Own Iterator in Python

class Counter:
    def __init__(self, maximum):
        self.maximum = maximum
        def __iter__(self):
            self.number = 0
            return self