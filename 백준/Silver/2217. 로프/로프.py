import sys
input = sys.stdin.readline

n = int(input())

ropes = []
for i in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)

weight = []
for i in range(n):
    weight.append(ropes[i]*(i+1))
    
print(max(weight))