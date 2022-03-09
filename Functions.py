# Simple Function
def function():
    print("Hello World")

#function()  # Calling a function


# Function with Arguments
def sumof(a, b):
    print(a + b)

#sumof(10, 24)


# *args unknown number of arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])
#my_function("Emil", "Tobias", "Linus")

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result
#print("\n\nRecursion Example Results")
#tri_recursion(6)

# Lambda function
x = lambda a : a * 10
print(x(5))

