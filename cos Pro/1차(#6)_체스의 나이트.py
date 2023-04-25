def solution(pos):

    directions = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]
    alpha = dict()
    for i in range(8):
        alpha[chr(65+i)] = i+1

    answer = 0
    for direction in directions:
        nx = alpha[pos[0]] + direction[0]
        ny = int(pos[1]) + direction[1]
        if 1<= nx <= 8 and 1<= ny <= 8:
            answer += 1

    return answer


pos = "A7"
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")