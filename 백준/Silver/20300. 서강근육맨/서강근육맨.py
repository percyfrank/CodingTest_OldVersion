n = int(input())
t = list(map(int,input().split()))

t.sort()

m = []
if n % 2 == 0:
    for i in range(n//2):
        m.append(t[i] + t[n-i-1])   
else:
    for i in range(n//2):
        m.append(t[i] + t[n-i-2])
        
print(max(m))