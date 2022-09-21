from collections import deque
import copy
import sys

input = sys.stdin.readline

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
    arr = copy.deepcopy(virus)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    queue.append((nx,ny))
    
    cnt = 0                
    for a in arr:
        cnt += a.count(0)
    ans = max(ans,cnt)

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if virus[i][j] == 0:
                virus[i][j] = 1
                wall(cnt+1)
                virus[i][j] = 0
                
wall(0)
print(ans)