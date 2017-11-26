a={'1':[1,2],'2':[2,3]}
b={}
for i in range(1,6):
    b[str(i)]=[i,2*i+1]
print(b)
for key in b:
    print("{} correspomd to {}".format(key,b[key]))