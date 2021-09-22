list=input("Enter the list").split(",")
print ("original list: " +  str(list))
lis = []
for i in list:
    if i not in lis:
        lis.append(i)
print ("list without duplicates: " + str(lis))
