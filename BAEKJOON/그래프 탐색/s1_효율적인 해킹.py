from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    cnt = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)    
    return cnt

arrays = []
idx = 0
for i in range(1,n+1):
    cnt = bfs(i)
    if cnt > idx:
        arrays.clear()
        arrays.append(i)
        idx = cnt
    elif cnt == idx:
        arrays.append(i)
    

print(*arrays)
    

