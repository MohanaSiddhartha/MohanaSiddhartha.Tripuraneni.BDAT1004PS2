def binary(n):
    num=n
    
    if(num==0):
        print(0 ,end =" "),
        return
    
    if(num==1):
        print(1, end =" "),
        return
    if(num%2==0):
        num=num/2
        binary(num)
        print(0, end =" "),
        return
    else:
        num=(num-1)/2
        (binary(num))
        print(1, end =" "),
        return
