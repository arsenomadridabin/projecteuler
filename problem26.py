def length_of_pattern(num):
        for i in range(len(num)):
            if(num[0:i+1])==(num[(i+1):(2*i+2)]):
                return i+1
        else:
            return 0

list2=[]
for i in range(2,1001):
    val=1/i
    val=str(val)
    splitter=val.split('.')
    list2.append(splitter[1])
dict2=[]
for i,x in enumerate(list2):
    a=length_of_pattern(x)
    dict2.append(a)
print(max(dict2))
