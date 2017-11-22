from math import pow
fp=open('data2.txt','r')
a=fp.read()
b=a.split('\n')
print(len(b))
num=[]
for i in b:
    c=i.split(' ')
    num.append(c)
new=[]
for i in num:
    for j in i:
        new.append(int(j))
sum=sum(new)

