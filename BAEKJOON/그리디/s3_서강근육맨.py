
n = int(input())
t = list(map(int,input().split()))

t.sort()

# 근손실 최솟값 리스트
m = []

# 운동기구 갯수가 짝수일 경우 
if n % 2 == 0:
    for i in range(n//2):
        m.append(t[i] + t[n-i-1])
# 홀수일 경우   
else:
    for i in range(n//2):
        m.append(t[i] + t[n-i-2])
        
print(max(m))