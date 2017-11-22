
# from functools import reduce
# def factors(n):
#     return set(reduce(list.__add__,
#                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
from math import sqrt
def factors(n):
    list1 = []
    for i in range(1,int(sqrt(n))+1):
        if(n%i==0):
            list1.append(i)
            list1.append(n/i)
    return list1
def triangle_number(num):
    return (num*(num+1))/2
i=1000
length=1
while(length<=500):
    triangle_num=triangle_number(i)
    length=len(factors(int(triangle_num)))
    i=i+1
print(triangle_num)
print(factors(644))