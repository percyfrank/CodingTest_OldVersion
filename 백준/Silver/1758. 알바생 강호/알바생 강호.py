import sys
input = sys.stdin.readline

n = int(input())
m = []
for i in range(n):
    m.append(int(input()))

m.sort(reverse=True)

tip = 0
for i in range(n):
    if m[i] - i < 0:
        pass
    else:
        tip += m[i] - i
    
print(tip)