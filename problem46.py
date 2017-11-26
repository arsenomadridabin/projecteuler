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
def check_issquare(num):
    a=sqrt(num)
    b=int(a)
    if(a==b):
        return True
prime_numbers=[]
composite_numbers=[]



num=3
def check(req_num):
    flag=0
    for i in prime_numbers:
        if i>req_num:
            break
        val=(req_num-i)/2
        if(check_issquare(val)):

            flag=1
    if(flag==1):
        return False
    else:
        return True
for i in range(3,1000000):
    if(is_prime(i)):
        prime_numbers.append(i)
    else:
        if i%2:
            composite_numbers.append(i)
composite_numbers=composite_numbers[6:]
for i in composite_numbers:
    if(check(i)):
        print(i)
        break


