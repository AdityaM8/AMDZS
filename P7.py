a=int(input("Enter lower limit:"))
b=int(input("Enter upper limit:"))
for n in range(a, b+1):
   if((n%7==0) & (n%5!=0)):
      print(n)
 
 
