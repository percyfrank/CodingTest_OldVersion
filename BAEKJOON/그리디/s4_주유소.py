import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int,input().split()))
price = list(map(int,input().split()))

# 두 번째 도시로 가기 위해선 첫 번째 주유소에서 반드시 기름을 넣어야 함
total = price[0] * road[0]

# 가장 작은 주유가격 저장
min_cost = price[0]

# 현재 도시의 주유가격과 비교
for i in range(1,n-1):
    if min_cost < price[i]:
        total += min_cost * road[i]
    # 현재 도시의 주유가격이 저렴하면 주유가격 변경
    else:
        min_cost = price[i]
        total += min_cost * road[i]
print(total)
          
        
