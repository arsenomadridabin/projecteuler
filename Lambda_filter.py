def check_prime(num):
    prime=True
    if num==1 or num==2:
        return True
    else:
        for i in range(2,num):
            if(num % i==0):
                prime=False
                break
        return prime
a=[i for i in range(1,1000)]
only_prime=filter(check_prime,a)
print(list(only_prime))
