def bubble(l):
    for i in range(len(l)-1,0,-1):
       
        for j in range(i):
           
            if l[j]>l[j+1]:
              l[j],l[j+1]=l[j+1],l[j]
    print ("Bubble sorted array is:",l)

def selection(a):
    for i in range (len(a)):
        minidex=i
        print (f"the array index is {i}")
        print("current array is :", a)

        for j in range(i,len(a)):
            if a[j]<a[minidex]:
                minidex=j
    
        t=a[i]
        a[i]=a[minidex]
        a[minidex]=t
    print("selection sorted array is:", a)



l=[6,3,5,4,1,7]
a=[8,10,6,4,2,3]
bubble(l)
selection(a)