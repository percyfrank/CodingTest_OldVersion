import sys


n = int(sys.stdin.readline().rstrip())

ropes = []
for i in range(n):
    ropes.append(int(sys.stdin.readline().rstrip()))

ropes.sort(reverse=True)

weight = []
for i in range(n):
    weight.append(ropes[i]*(i+1))
    
print(max(weight))
    
    