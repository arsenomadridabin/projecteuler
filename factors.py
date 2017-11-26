# def factors(num):
#     divisors=[]
#     for i in range(1,int(num/2)+1):
#         if not num%i:
#             divisors.append(i)
#     divisors.append(num)
#     return divisors
# print(factors(50005000))
# from functools import reduce
# def factors(n):
#     return set(reduce(list.__add__,
#                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
# print(len(factors(50005000)))
from math import sqrt
def factors(n):
    list1 = []
    for i in range(1,int(sqrt(n))+1):
        if(n%i==0):
            list1.append(i)
            list1.append(n/i)
    return list(set(list1))

print(factors(644))
