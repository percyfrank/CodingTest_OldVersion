
def solve(start):
    if len(answer) == m:
        print(*answer)
        return
    for num in range(1, n+1):
        if not visited[num]:
            visited[num] = True
            answer.append(num)
            solve(start)
            visited[num] = False
            answer.pop()

n,m = map(int,input().split())
visited = [False] * (n+1)
answer = []
solve(1)