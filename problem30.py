num=32
list1=[]
count=0
a=5*pow(9,5)
while(count<a):
    sum1=0
    num_rep=num
    while(num!=0):
        rem=num %10
        sum1=sum1+pow(rem,5)
        num=int(num/10)
    if(sum1==num_rep):
        list1.append(num_rep)
    num=num_rep+1
    count=count+1
print(sum(list1))


