n = int(input())

a = []
for i in range(14):
    a.append(list(map(int,input().split())))
    
tmp = 0
cnt = 0
for i in range(len(a)):
    tmp = n // a[i]
    n -= tmp*a[i]
    if n == 0:
        