from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
result = [[0] * n for _ in range(n)]

def bfs(node):
    q = deque()
    q.append(node)
    while q:
        next = q.popleft()
        for i in range(n):
            if not visited[i] and graph[next][i] == 1:
                visited[i] = True
                q.append(i)
                result[node][i] = 1

for i in range(n):
    visited = [False] * n
    bfs(i)

for i in result:
    print(*i)

