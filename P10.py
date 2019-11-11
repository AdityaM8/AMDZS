n=int(input("Enter how many nos"))
numbers=[]
for i in range(1,n+1):
    x=int(input("Enter no"))
    numbers.append(x)
even=[]
odd=[]
for y in numbers:
       if(y%2==0):
        even.append(y)
       else:
        odd.append(y)
print(numbers)
print(odd)
print(even)
