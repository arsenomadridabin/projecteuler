from math import sqrt
def factors(n):
    list1 = []
    for i in range(1,int(sqrt(n))+1):
        if(n%i==0):
            list1.append(i)
            list1.append(n/i)
    list1.remove(n)
    return sum(list(set(list1)))

def expressed_as_abundant(num,abundant):
    for i in abundant:
        val = str(num-int(i))
        if(val in abundant):
            return True
    return False

abundant={}
for i in range(12,28124):
    fact_sum=factors(i)
    if(fact_sum>i):
        abundant[str(i)]=True

print(abundant)
sum1=0
for i in range(25,28124):
    if not expressed_as_abundant(i,abundant):
        sum1=sum1+i
print(sum1)
