fp=open("data18.txt","r")
data = [[int(x) for x in y.strip().split(' ')] for y in fp.readlines()]
print(data)

assert False
def maxnum(a,b):
    if(a>b):
        return a
    else:
        return b

for i in range(1,15):
    for j in range(i+1):
        if(j==0):
            new_list[i][j]=int(new_list[i][j])+int(new_list[i-1][j])
        elif(j==i):
            new_list[i][j]=int(new_list[i][j])+int(new_list[i-1][j-1])
        else:
            new_list[i][j]=int(new_list[i][j])+maxnum(int(new_list[i-1][j-1]),int(new_list[i-1][j]))
print(max(new_list[14]))

