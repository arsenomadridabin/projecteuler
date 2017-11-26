from math import sqrt
import time
def check_area_integer(num):
    val1=sqrt(3*num*num+2*num-1)/4
    if(val1==int(val1)):
        return True, num-1
    val2=sqrt(3*num*num-2*num-1)/4
    if(val2==int(val2)):
        return True,num+1
    else:
        return False,0
perimeter=0
list1=[(i*(i-1)/2)+(i+1)/2 for i in range(3,100000,2)]
print(list1)
for i in list1:
    a=time.time()
    bool1,val=check_area_integer(i)
    print(bool1)
    if(bool1):
        print(i)
        perimeter = perimeter + (2 * i + val)
    b=time.time()
print(perimeter,b-a)





