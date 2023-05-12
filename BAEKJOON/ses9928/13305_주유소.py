
n = int(input())
roads = list(map(int,input().split()))
oils = list(map(int,input().split()))
oils = oils[:n-1]
MIN = min(oils)
answer = 0

if oils[0] == MIN:
    answer = oils[0] * sum(roads)
else:
    answer += oils[0] * roads[0]
    MIN = oils[0]
    for i in range(1,n-1):
        if oils[i] > MIN:
            answer += MIN * roads[i]
        else:
            answer += oils[i] * roads[i]
            MIN = oils[i]

print(answer)