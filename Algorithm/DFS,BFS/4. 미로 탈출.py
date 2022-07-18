from collections import deque

n,m = map(int,input().split())

# 2차원 맵 0으로 초기화 후 입력 받기
graph = [[0]*m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int,input()))
    
# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵을 벗어나거나 괴물이 있는 곳일 경우 무시
            if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] == 0:
                continue             
            # 해당 위치를 처음 방문하는 경우에만 거리 +1 기록
            if graph[x][y] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
                
    return graph[n-1][m-1]


print(bfs(0,0))

