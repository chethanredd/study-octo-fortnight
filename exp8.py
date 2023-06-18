import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
import math

def mergesort(my_list):
    if len(my_list)>1:
        mid=len(my_list)//2
        left=my_list[:mid]
        right=my_list[mid:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i]<=right[j]:
                my_list[k]=left[i]
                i+=1
            else:
                my_list[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            my_list[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            my_list[k]=right[j]
            j+=1
            k+=1

my_list=[34,56,67,35,76,35,78,45,90,21]
print("before sorting",my_list)
mergesort(my_list)
print("After sorting", my_list)

x=list(range(1,10000))
plt.plot(x, [y*math.log(y, 2)for y in x])
plt.title("Merge Sort")
plt.xlabel("Input")
plt.ylabel("time")
plt.show()