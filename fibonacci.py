from math import pi


def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    count =2 
    if n>0:      
        for i in range(2,n):
            if count !=10:
                c =a+b
                b = c 
                a = b
                print(c)
                count = count +1 
                
    else:
        print("enter positive number ")
    print("count : ",count)


fibonacci(15)