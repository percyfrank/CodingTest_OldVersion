import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int,input().split()))
price = list(map(int,input().split()))
    
result = price[0] * road[0]
for i in range(n-2):
    if price[i] < price[i+1]:
        result += price[i] * road[i+1]
    else:
        result += price[i+1] * road[i+1]   

print(result)