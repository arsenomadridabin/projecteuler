list1=[[0]*21 for i in range(21)]
for i in range(21):
    list1[i][20]=1
    list1[20][i]=1
for i in range(19,-1,-1):
    for j in range(19,-1,-1):
        list1[i][j]=list1[i][j+1]+list1[i+1][j]
print(list1[0][0])