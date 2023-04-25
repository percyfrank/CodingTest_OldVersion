

def solution(commands):

    direction = dict()
    direction['U'] = [0,1]
    direction['D'] = [0,-1]
    direction['L'] = [-1,0]
    direction['R'] = [1,0]

    x,y = 0,0
    for command in commands:
        x = x + direction[command][0]
        y = y + direction[command][1]
    answer = [x,y]

    return answer


commands = "URDDL"
ret = solution(commands)

print("solution 함수의 반환 값은", ret, "입니다.")