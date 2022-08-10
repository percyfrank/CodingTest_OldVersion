from collections import deque

n,m = map(int,input().split())

virus = [[0]*m for _ in range(n)]

for i in range(n):
    virus[i] = list(map(int,input().split()))
    

queue = deque()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

ans = 0

def bfs():
    
    global ans
    for i in range(n):
        for j in range(m):
            if virus[i][j] == 2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if virus[nx][ny] == 0:
                    virus[nx][ny] = 2
                    queue.append((nx,ny))
    
    cnt = 0                
    for viruss in virus:
        cnt += virus.count(0)
    max(ans,cnt)


cnt = 0
for i in range():
    for j in range():
        if virus[i][j] == 0:
            cnt += 1

print(cnt)
    