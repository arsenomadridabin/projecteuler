list1=[]
mat=[]
for i in range(1001):
    for j in range(1001):
        list1.append(0)
    mat.append(list1)
    list1 = []
i=500
j=500
mat[i][j]=1
moving_to="right"
while(mat[0][1000]==0):
    if(moving_to=="right" and mat[i][j+1]==0):
        j=j+1
        mat[i][j]=mat[i][j-1]+1
        if(mat[i+1][j]==0):
            moving_to="down"
        else:
            moving_to="right"
    if(moving_to=="down" and mat[i+1][j]==0):
        i=i+1
        mat[i][j]=mat[i-1][j]+1
        if(mat[i][j-1]==0):
            moving_to="left"
        else:
            moving_to="down"
    if (moving_to == "left" and mat[i][j-1] == 0):
        j=j-1
        mat[i][j] = mat[i][j+1] + 1
        if (mat[i-1][j] == 0):
            moving_to = "up"
        else:
            moving_to = "left"
    if (moving_to == "up" and mat[i-1][j] == 0):
        i=i-1
        mat[i][j] = mat[i+1][j] + 1
        if (mat[i][j+1] == 0):
            moving_to = "right"
        else:
            moving_to = "up"
sum=0
for i,x in enumerate(mat):
    for j,y in enumerate(x):
        if(i==j or i+j==1000):
            sum=sum+y
print("Sum=",sum)





