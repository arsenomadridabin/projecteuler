for i in range(1,1001):
    for j in range(i+1,1001):
        c=1000-i-j
        if(pow(i,2)+pow(j,2))==pow(c,2):
            print(i*j*c)

