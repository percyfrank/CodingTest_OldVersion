
def solve(start):
    global cnt
    if sum(answer) == s and len(answer) > 0:
        cnt += 1
    for i in range(start,n):
        answer.append(arr[i])
        solve(i+1)
        answer.pop()
    return cnt

n,s = map(int,input().split())
arr = list(map(int,input().split()))
answer = []
cnt = 0
print(solve(0))


