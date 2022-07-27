n = int(input())

graphs = [[0]*n for _ in range(n)]
for i in range(n):
    graphs[i] = list(map(int,input()))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0

def dfs(x,y):
    
    if x < 0  or x >= n or y < 0 or y >= n:
        return False
    
    if  graphs[x][y] == 1:
        global count
        count += 1
        graphs[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)           
        return True
    
    return False

result = 0
array = []

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            array.append(count)
            result += 1
            count = 0

print(result)
array.sort()
for i in range(len(array)):
    print(array[i])