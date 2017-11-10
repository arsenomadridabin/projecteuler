import time
def prime_factors(n):
    list1=[]
    i = 1
    while (i <= n):
        k = 0
        if (n % i == 0):
            j = 1
            while (j <= i):
                if (i % j == 0):
                    k = k + 1
                j = j + 1
            if (k == 2):
                list1.append(i)
        i = i + 1

    return list1
a=time.time()
print(prime_factors(10000001))
b=time.time()
print(b-a)