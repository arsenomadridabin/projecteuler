import time

def get_chain_length(num):
    count=1
    while(num!=1):
        if not num%2:
            num=num/2
            count=count+1
        else:
            num=3*num+1
            count=count+1
    return count
list1=[]
for i in range(1,1000000):
    chain_length=get_chain_length(i)
    # if(chain_length)==525:
    #     print("number=",i)
    #     break
    list1.append(chain_length)
max_num=max(list1)
t1=time.time()
a=[i for i,x in enumerate(list1) if x == max_num]
t2=time.time()
print("diff",t2-t1)
print(a)
