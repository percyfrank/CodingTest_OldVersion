
input_data = input()

row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동 가능한 방향
steps = [(2,1),(2,-1),(-2,-1),(-2,1),(-1,-2),(1,-2),(1,2),(-1,2)]

count = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    # 해당 위치 이동 가능 시 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        count += 1 

print(count)