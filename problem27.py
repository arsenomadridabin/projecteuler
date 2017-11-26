from math import sqrt
def is_prime(num):
    flag=0
    for i in range(2,int(sqrt(num))+1):
        if not num%i:
            flag=1
            break
    if(flag==1):
        return False
    else:
        return True
list1=[0]
list2=[0]
func=lambda x,a,b: x*x +a*x +b
for a in range(1000):
    for b in range(1001):

        for i in range(4):
            count = 0
            while(1):
                if(i==0):
                    val=func(count,-a,-b)
                elif(i==1):
                    val = func(count, -a, b)
                elif(i==2):
                    val = func(count, a, -b)
                else:
                    val = func(count,a,b)
                if(val<2):
                    break
                if(is_prime((val))):
                    count=count+1
                else:
                    break
            if(count>list1[0]):
                list1[0]=count
                if(i==0):
                    list2[0]=a*b
                elif(i==1):
                    list2[0] = -a * b
                elif(i==2):
                    list2[0] = -a * b
                else:
                    list2[0] = a * b
print("Longest series is {} and product is {} ".format(list1[0],list2[0]))
