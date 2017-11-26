import re
fp=open('data2.txt','r')
a=fp.read()
data=re.findall(r"[\w']+",a)
list1=[]
for i in range(15):
    list1.append(data[15*i:15*(i+1)])
print(list1)
