from itertools import permutations
list1=[1,2,3,4,5,6,7,8,9]
a=list(permutations(list1,2))
b=list(permutations(list1,3))
c=list(permutations(list1,1))
d=list(permutations(list1,4))
numbers = []
sum=0
list2=[]
for count,i in enumerate(a):
	for j in b:
		
		val = int(str(i[0])+str(i[1])) * int( str(j[0])+str(j[1])+str(j[2]))
		numbers.extend(list(i))
		numbers.extend(list(j))
		duplicate=val
		while(val!=0):
			num = val % 10
			numbers.append(num)
			val=int(val/10)
		if len(numbers) == len(list(set(numbers))) and 0 not in numbers:
			sum=sum + duplicate
			print(numbers)
			list2.append(numbers)	
		numbers=[]
for count,i in enumerate(c):
	for j in d:
		
		val = int(str(i[0])) * int( str(j[0])+str(j[1])+str(j[2])+str(j[3]))
		numbers.extend(list(i))
		numbers.extend(list(j))
		duplicate=val
		while(val!=0):
			num = val % 10
			numbers.append(num)
			val=int(val/10)
		if len(numbers) == len(list(set(numbers))) and 0 not in numbers:
			sum=sum + duplicate
			print(numbers)
			list2.append(numbers)	
		numbers=[]
print("ist2",list2)
list3=[]
for i in list2:
	val=i[-4:]
	val2=int(str(val[3])+str(val[2])+str(val[1])+str(val[0]))
	list3.append(val2)
val=list(set(list3))
sum=0
for i in val:
	sum=sum+i
print(sum)


			


