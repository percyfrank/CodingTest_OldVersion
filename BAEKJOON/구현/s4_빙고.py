
def line_bingo():
    bingo = 0
    for i in range(5):
        flag1 = True
        flag2 = True
        for j in range(5):
            if check[i][j] == 0:
                flag1 = False
            if check[j][i] == 0:
                flag2 = False
        if flag1: 
            bingo += 1
        if flag2:
            bingo += 1                      
    return bingo

def diagonal_bingo():
    bingo = 0
    flag1 = True
    flag2 = True
    for i in range(5):
        if check[i][i] == 0:
            flag1 = False
        if check[i][4-i] == 0:
            flag2 = False
    if flag1: 
        bingo += 1
    if flag2:
        bingo += 1                      
    return bingo


index = dict()
check = [[0]*5 for _ in range(5)]

for i in range(5):
    array = list(map(int,input().split()))
    for j in range(5):
        index[array[j]] = i,j

cnt = 0       
for _ in range(5):
    array = list(map(int,input().split()))
    for i in range(5):
        cnt += 1
        
        if array[i] in index:
           check[index[array[i]][0]][index[array[i]][1]] = 1
           
           if (line_bingo() + diagonal_bingo()) >= 3:
               print(cnt)
               exit()
    


    
    
    
    
