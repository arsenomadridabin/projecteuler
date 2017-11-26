def le_sum(str):
    a=0
    for i in range(len(str)):
        a=a+ord(str[i])-64
    return a


fp=open("data22.txt","r")
a=fp.readlines()
list1=[]
c=a[0].split(",")
list1=[ i.replace('"','') for i in c]
list1.sort()
a=[le_sum(i) for i in list1]
print(a)
b=[x*(i+1) for i,x in enumerate(a)]
print(sum(b))
