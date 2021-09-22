def vow(v):
    return ((v == 'a')
            or
            (v == 'e')
            or 
            (v == 'i')
            or
            (v == 'o')
            or 
            (v == 'u'));
def removeconvow(str):
    print(str[0], end ="");
    for i in range(1,len(str)):
        if((vow(str[i - 1])!= True) or (vow(str[i])!= True)):
         print(str[i], end = "");
str= input("Enter a string:");
removeconvow(str);
