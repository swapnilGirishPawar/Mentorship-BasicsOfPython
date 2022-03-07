#Variables
"""
number = 10
String = "Swapnil_Pawar"
print(number)
print(String)

# Integer number
num = 100
print(num)
print("Data Type of variable num is", type(num))

# float number
fnum = 34.45
print(fnum)
print("Data Type of variable fnum is", type(fnum))


# Python program to print strings and type
s = "This is a String"
s2 = 'This is also a String'

# displaying string s and its type
print(s)
print(type(s))

# displaying string s2 and its type
print(s2)
print(type(s2))


# tuple of integers
t1 = (1, 2, 3, 4, 5)
# prints entire tuple
print(t1)

# tuple of strings
t2 = ("hi", "hello", "bye")
# loop through tuple elements
for s in t2:
    print (s)

# tuple of mixed type elements
t3 = (2, "Lucy", 45, "Steve")
print(t3[2])

# list of integers
lis1 = [1, 2, 3, 4, 5]
# prints entire list
print(lis1)
# list of strings
lis2 = ["Apple", "Orange", "Banana"]
# loop through list elements
for x in lis2:
    print (x)
# List of mixed type elements
lis3 = [20, "Chaitanya", 15, "BeginnersBook"]
print("Element at index 3 is:",lis3[3])

# Dictionary example

dict = {1:"Chaitanya","lastname":"Singh", "age":31}

# prints the value where key value is 1
print(dict[1])
# prints the value where key value is "lastname"
print(dict["lastname"])
# prints the value where key value is "age"
print(dict["age"])
"""
# Set Example
myset = {"hi", 2, "bye", "Hello World"}

# loop through set
for a in myset:
    print(a)

# checking whether 2 exists in myset
print(2 in myset)

# adding new element
myset.add(99)
print(myset)