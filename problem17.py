mul=1
for i in range(1,101):
    mul=mul*i
sum=0
while(mul!=0):
    sum=sum+(mul%10)
    mul=int(mul/10)
print(sum)