def total_num(a,b,c):
    list1=[]
    while(a!=0):
        c=a % 10
        a=int(a/10)
        list1.append(c)
    while(b!=0):
        e= b % 10
        b= int (b/10)
        list1.append(e)
    if(len(list1) == len(set(list1))):
        while(c!=0):
            f= c % 10
            c= int (c/10)
            list1.append(f)
    if(len(list1)==len(set(list1))):
        return True
    else:
        return False
list2=[]
for i in range(11,100):
    for j in range(111,1000):
        val=total_num(i,j,i*j)
        if val:
            list2.append(i*j)
print(list2)

