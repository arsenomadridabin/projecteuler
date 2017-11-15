from math import sqrt
def is_prime(num):
    flag=0
    for i in range(2,int(sqrt(num))+1):
        if not num%i:
            flag=1
            break
    if(flag==1):
        return False
    else:
        return True
sum=0
for i in range(2,2000001):
    if(is_prime(i)):
        sum=sum+i
print(sum)
