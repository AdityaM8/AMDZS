def samebysinflip(str):
    str=input("Enter the binary sequence")
    zero = 0
    one = 0
    for i in range(0, len(str)):
        ch = str[i];
        if (ch == '0'):
            zero = zero + 1
        else:
            one = one + 1
    return (zero == 1 or one == 1);
if(samebysinflip(str)):
    print("YES")
else:
    print("No")
