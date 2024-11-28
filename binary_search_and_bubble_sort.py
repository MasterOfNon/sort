#from numpy import *
def sorting (a):
    l=len(a)
    for i in range (l):
        for j in range(l-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
def binsearch(a,l,u):
    si=int( input("enter the serach item:"))
    while l<=u:
        mid=(l+u)//2
        if a[mid]==si:
            return mid
        elif si<a[mid]:
            u=mid-1
        else:
            l=mid+1



        
#a=array([]) array cannot be left empty so make it list and convert it into array
a=[]
r= int (input("enter the size of list:"))
for i in range(r):
    x= int(input(f"enter the  value for index {i+1}:"))
    a.append(x)
print("array is:",a)
#a=array(a) since in array python swapping does not work i am skipping this

newa=sorting(a)
l=0
u=r-1
ind=binsearch(newa,l,u)
print(f"Search item found at index {ind}")