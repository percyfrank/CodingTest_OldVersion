from collections import deque

n = int(input())

graph = [[0]*n for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int,input()))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    count = 0
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == 0:
                continue     
                    
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
    return count

array = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            array.append(bfs(i,j))
        count = 0
        
array.sort()       
print(len(array))
for i in range(len(array)):
    print(array[i])
        