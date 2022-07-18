

n = int(input())
plans = input().split()
x, y = 1, 1

# 계획서 내용에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            x = x + dx[i]
            y = y + dy[i]
            # 공간을 벗어나면 이전 단계로 돌려놓기
            if x < 1 or x > n or y < 1 or y > n:
                x = x - dx[i]
                y = y - dy[i]
                                    
print(x,y)
            
        
        