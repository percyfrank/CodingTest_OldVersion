
n = int(input())
m = int(input())

# 0부터 시작하기 때문에 n+1
graph = [[] for _ in range(n+1)]

# 노드 연결 정보
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

count = -1 #자기 자신의 노드도 포함하기 때문에 0이 아닌 -1부터 시작
for i in range(len(visited)):
    if visited[i] == True:
        count += 1
print(count)