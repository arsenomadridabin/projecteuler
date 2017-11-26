import math
def sum_of_digits(num):
    sum = 0
    while ( num != 0 ):
        rem = num % 10
        sum = sum + rem
        num = int( num / 10)
    return sum
list1=[]
for i in range(2,135):
    for j in range(2,30):
        a=pow(i,j)
        if(sum_of_digits(a)==i):
            list1.append(a)
list1.sort()
print(list1[29])
