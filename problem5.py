def generate_factors(num):
    list1=[]
    i=2
    while(i<=num):
        if(num%i)==0:
            list1.append(i)
            i=i-1
            num=num/2
        i=i+1
    return list1
print(generate_factors(24))

num=2
i=3
while(i<=20):
    if (num%i!=0):
        fact=generate_factors(i)
        for j in fact:
            num=num*j
            if(num%i==0):
                break
    i=i+1
print(num)
