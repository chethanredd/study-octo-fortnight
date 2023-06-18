import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

def selectionsort(a):
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(i+1, n):
         if a[j]<a[min]:
            a[j], a[min]=a[min], a[j]

a=[32,43,34,24,65,54,45]
print("Before sorting", a)
selectionsort(a)
print("After sorting", a)

x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("selection sort time complexity o(n)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
