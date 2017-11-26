from functools import reduce
list1=[1,2,3,3,4,2,0,8,4,2]
sorted=[]
while(len(list1) !=0):
    greatest = reduce(lambda x, y: x if (x > y) else y, list1)
    list1.remove(greatest)
    sorted.append(greatest)
print(sorted)

