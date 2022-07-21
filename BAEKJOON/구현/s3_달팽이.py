'''
* 홀수인 자연수가 주어지면 달팽이 모양으로 숫자 출력

* 방향 설정 후, 방향대로 이동했을 때 장애물이 있으면 방향 수정하는 느낌으로 풀기
'''

import sys
input = sys.stdin.readline

N = int(input())
p = int(input())


arrays = [[0]*N for _ in range(N)]

# 방향은 고정(하 우 상 좌)
dx = [1,0,-1,0]
dy = [0,1,0,-1]

n = N**2
x,y = 0,0
arrays[0][0] = n

# 숫자 p의 인덱스
X,Y = 0,0

i = 0
while n > 1:
    
    nx = x + dx[i]
    ny = y + dy[i]  

    if nx <= N-1 and ny <= N-1 and nx >= 0 and ny >= 0 and arrays[nx][ny] == 0:
        arrays[nx][ny] = n-1
        if n-1 == p:
            X = nx
            Y = ny
        x = nx
        y = ny
        n -= 1

    else:
        i = (i+1) % 4

for array in arrays:
    print(*array)

'''
* 이렇게 하면 시간 더 걸림
for i in range(N):
    for j in range(N):
        print(array[i][j], end = " ")
    print()
'''

    
print(X+1,Y+1)        

    
        
        
        
        

