def dec_to_binary(num):
	string=[]
	while(num!=0):
		rem = num % 2
		string.append(str(rem))
		num = int(num/2)
	return string
a=dec_to_binary(8)

def check_palindrome(num):
	if(num == num[::-1]):
		return True

sum1=0
for i in range(1,1000001):
	if check_palindrome(str(i)):
		val = dec_to_binary(i)
		val_str= ''.join(val)
		if check_palindrome(val_str):
			sum1=sum1+i

print(sum1)	

		  
