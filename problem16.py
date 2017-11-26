from math import pow

a=int(pow(2,1000))
b=str(a)

print(a)
sum=0
while(a!=0):
    sum=sum+(a%10)
    a=int(a/10)
print(sum)