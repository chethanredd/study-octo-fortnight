import math

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

def binaryrecursion(a,low, high, key):
    if low<=high:
        mid=(high+low)//2
        if a[mid]==key:
            print("search successful, key found at the location :", mid+1)
            return
        elif key<a[mid]:
            return binaryrecursion(a,low,mid-1,k)
        elif key>a[mid]:
            return binaryrecursion(a,mid+1,high,k)
    else:
        print("Search successful")

a=[13,34,56,78,85,77,33]
print("The array elements are:",a)
k=34
binaryrecursion(a,0,len(a)-1,k)

x=list(range(1,10000))
plt.plot(x, [math.log(y, 2) for y in x])
plt.title("Binary Recursion")
plt.xlabel("input")
plt.ylabel("time")
plt.show()