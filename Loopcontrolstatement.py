#break statement
"""
count = 0
while count <= 100:
      print (count)
      count += 1
      if count >= 3:
            break

#Pass Statement
for letter in 'SwapnilP':
   if letter == 'i':
      pass
      print ('Pass block')
   print ('Current letter is:', letter)
"""
#Continue Statement
for x in range(10):
   #check whether x is even
   if x % 2 == 0:
      continue
   print (x)