x=input("Enter the number")
y=int(x)
if y > 1:
   for i in range(2,y):
       if (y%i)==0:
           print(y,"is not a prime number")
           break
   else:
       print(y,"is a prime number")
else:
   print(y,"is not a prime number")
