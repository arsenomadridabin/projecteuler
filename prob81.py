
def minimum(a,b):
    if(a<b):
        return a
    else:
        return b
a=open("data2.txt",'r')
count=0
list1=[]
list2=[]
#parsing
for i in a:
    spliter=i.split('\n')
    list1.append(spliter[0])
for i in list1:
    b=i.split(',')
    c=[]
    for k in b:
       c.append(int(k))
    list2.append(c)

for i in range(78,-1,-1):
    list2[79][i]=list2[79][i]+list2[79][i+1]
    list2[i][79]=list2[i][79]+list2[i+1][79]
print(list2)
for i in range(78,-1,-1):
    for j in range(78,-1,-1):
        list2[i][j]=list2[i][j]+minimum(list2[i+1][j],list2[i][j+1])
print(list2)