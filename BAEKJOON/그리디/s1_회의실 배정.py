'''

* 회의 시작시간, 끝나는 시간 입력받기 
 
* 입력받은 회의를 1. 끝나는 시간 2. 시작 시간 순으로 정렬

'''



import sys
input = sys.stdin.readline

n = int(input())
meeting = []

for _ in range(n):
    start,end = map(int,input().split())
    meeting.append([start, end])
    
meeting = sorted(meeting, key=lambda a: (a[1],a[0])) 

count = 0
time = 0

for i,j in meeting:
    if i >= time:
        count += 1
        time = j        

print(count)
         


        