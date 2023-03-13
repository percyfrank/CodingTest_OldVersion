
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
  
visited = [False] * (n+1)

def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
dfs(graph,1,visited)

count = -1
for i in range(len(visited)):
    if visited[i] == True:
        count += 1
print(count)