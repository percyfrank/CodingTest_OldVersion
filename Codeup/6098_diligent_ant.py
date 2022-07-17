
d = [[0]*10 for _ in range(10)]

for i in range(10):
    d[i] = list(map(int,input().split()))
    
x,y = 1,1   
while True:
    if d[x][y] == 2:     
        d[x][y] = 9
        break;
    
    if d[x][y+1] != 1:        # 오른쪽에 벽이 없을 경우
        d[x][y] = 9
        y += 1    
    else:                     # 오른쪽에 벽이 있을 경우
        if d[x+1][y] != 1:    # 오른쪽에 벽이 있고, 아래에는 벽이 없을 경우
            d[x][y] = 9
            x += 1
        else:                 # 오른쪽, 아래쪽 벽이 모두 있을 경우
            d[x][y] = 9
            break;
         
for i in range(10):
    for j in range(10):
        print(d[i][j], end = ' ')
    print()

