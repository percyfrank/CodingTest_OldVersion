import sys
input = sys.stdin.readline

n = int(input())
time = []

for _ in range(n):
    start, end = map(int,input().split())
    time.append([start,end])
    
time.sort()


count = 1
idx = 0
for i in range(n):
    for j in range(i+1,n):
        if time[i][1] == time[j:][0]:
            count += 1
        

    