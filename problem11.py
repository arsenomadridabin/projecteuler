fp=open('nu,.txt','r')
a=fp.read()
b=a.split('\n')
num=[]
for i in b:
    c=i.split(' ')
    num.append(c)
list2=[]
for i in range(17):
    for j in range(17):
        product=int(num[i][j])*int(num[i+1][j+1])*int(num[i+2][j+2])*int(num[i+3][j+3])
        list2.append(product)
for i in range(17):
    for j in range(3,20):
        product=int(num[i][j])*int(num[i+1][j-1])*int(num[i+2][j-2])*int(num[i+3][j-3])
        list2.append(product)
print(max(list2))


