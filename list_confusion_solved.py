list1=[]
list2=[]
for i in range(10):
    for j in range(10):
        list1.append(1)
    list2.append(list1)
    list1=[]
print(list2)