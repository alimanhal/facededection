from array import *
pos =-1

def search(x,n):
    i =0
    while i<len(x):
        if x[i] ==n:
            globals()['pos'] = i
            return True
        i = i+1
    return False

x=[1,2,3,4,5]
n=4

if search(x , n):
    print("found at :  ", pos+1)
else:
    print("not found ")