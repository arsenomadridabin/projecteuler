list1=[]
for i in range(2,101):
    for j in range(2,101):
        list1.append(pow(i,j))
a=len(list(set(list1)))
print(a)