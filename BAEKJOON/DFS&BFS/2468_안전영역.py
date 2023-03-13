from collections import deque

n = int(input())

graph = []
max_h = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        max_h = max(max_h, graph[i][j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] > h:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


h_result = 0
for h in range(max_h):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] == 0:
                bfs(i, j, h)
                cnt += 1
    h_result = max(h_result,cnt)

print(h_result)
