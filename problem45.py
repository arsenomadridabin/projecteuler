import time
def generate_factors(num):
    list1=[]
    i=2
    while(i<=num):
        if(num%i)==0:
            list1.append(i)
            i=i-1
            num=num/(i+1)
        i=i+1
    return list(set(list1))
a=time.time()
i=10000
flag=0
while(1):
    if (flag == 0):
        count = 0
    if(len(generate_factors(i))==4):
        count=count+1
        flag=1
    else:
        flag=0
    if(count==4):
        print(i-3)
        break
    i=i+1
b=time.time()
print("time taken",b-a)


