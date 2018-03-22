import math
def is_prime(num):
	flag=0
	if num==1:
		return False
	for i in range(2,int(math.sqrt(num))+1):
		if num % i ==0:
			flag=1
			break
	if not flag:
		return True
	else:
		return False
val=11
def strip(val):
	val_list = []
	new_val = val
	for i in range(2):
		while(new_val!=0):
			new_val = int(new_val / 10)
			if new_val:
				val_list.append(new_val)
		new_val = int(str(val)[::-1])
	val_list.sort()
	return val_list

i=0   
while(1):
	if not i:
		val=11
		count=0
		sum1=0
	if(is_prime(val)):
		print(val)
		values = strip(val)
		if val==3797:
			print(values)
		flag =0
		for value in values:
			if not is_prime(value):
				flag=1
				break
		if not flag:
			count = count +1 
			sum1 = sum1 + val
	val = val + 2
	i=i+1
	if count==10:
		break
print("sum=",sum1)

 		
		

	
