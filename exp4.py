import matplotlib
import matplotlib.pyplot as py
matplotlib.use("TKAgg")

def linearsearch(a,key):
    n=len(a)
    for i in range (n):
        if a[i] == key:
            print("search successful key found at locate at:", i+1)
            return
    print("Search unsuccessful")

a=[23,54,53,67,22,54,56,82]
print("the array elements are:", a)
k=int(input("Enter the number to search" ))
linearsearch(a,k)

x=list(range(1,10000))
py.plot(x, [y for y in x])
py.title("Linear search time complexity is 0(n)")
py.xlabel("input")
py.ylabel("time")
py.show()