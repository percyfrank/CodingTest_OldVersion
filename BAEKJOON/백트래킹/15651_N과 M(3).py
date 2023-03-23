
def solve():
    if len(answer) == m:
        print(*answer)
        return
    for num in range(1,n+1):
        answer.append(num)
        solve()
        answer.pop()

n,m = map(int,input().split())
answer = []
solve()