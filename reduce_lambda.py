from functools import reduce
list1=[i for i in range(1,101)]
greatest=reduce(lambda x,y : x if(x>y) else y, list1)
print(greatest)