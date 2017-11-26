a=open("data83.txt",'r')
count=0
list1=[]
list2=[]
#parsing
for i in a:
    spliter=i.split('\n')
    list1.append(spliter[0])
for i in list1:
    b=i.split(',')
    c=[]
    for k in b:
       c.append(int(k))
    list2.append(c)

array1=[]
array2=[]
def find_next_node(current_node):
    cost_right=current_node.cost+current_node.right
class Node():
    objec_right=None
    objecct_left=None
    object_up=None
    object_down=None
    def __init__(self,right,left,up,down,cost,traverse):
        self.right=right
        self.left=left
        self.up=up
        self.down=down
        self.cost=cost
        self.traverse=traverse

for i in range(80):
    for j in range(80):
        if(j!=0):
            left=list2[i][j-1]
        else:
            left=None
        if(i!=0):
            up=list2[i-1][j]
        else:
            up=None
        if(j!=79):
            right=list2[i][j+1]
        else:
            right=None
        if(i!=79):
            down=list2[i+1][j]
        else:
            down=None
        object=Node(right=right,left=left,up=up,down=down,traverse=False,cost=100000000,i=i,j=j)

        array2.append(object)
    array1.append(array2)
    array2=[]
array1[0][0].traverse=True
array1[0][0].cost=0


while(array1[79][79].traverse==False):
    current_node=array1[0][0]
    next_node=find_next_node(current_node)

# print(array1[79][2].up,array1[79][2].right,array1[79][2].down,array1[79][2].left)

        # if(i==0):
        #     flag1=1
        # if(j==0):
        #     flag2=1
        # if(flag1==1 and flag2 != 1):
        #     a=Node(left=list2[i][j],right=list2[i][j+1],up=None,down=[i+1][j],cost=1000000,traverse=False)
        # elif(flag2==1 and flag1 !=1):
        #     a = Node(left=None, right=list2[i][j + 1], up=[i][j], down=[i + 1][j], cost=1000000, traverse=False)
        #     a=Node(right=list2[i][j+1],)
        # elif(flag1==1 and flag2==1):
        #





