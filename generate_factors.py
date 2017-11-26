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
    return list1
a=time.time()
print(generate_factors(1301081))
b=time.time()
print(b-a)