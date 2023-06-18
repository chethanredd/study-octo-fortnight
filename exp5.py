import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TKAgg")

def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

a=[3,34,45,23,45,26,63,44,56,7,568,97]
print("before sorting", a)
bubblesort(a)
print("after sorting", a)

x=list(range(1,1000000))
plt.plot(x, [y*y for y in x])
plt.title("Bubble Sort")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()