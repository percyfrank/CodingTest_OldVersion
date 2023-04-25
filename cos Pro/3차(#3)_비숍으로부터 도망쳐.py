

def solution(bishops):

    alpha = dict()
    for i in range(8):
        alpha[chr(65+i)] = i+1

    visited = set()
    directions = [[1,1],[1,-1],[-1,-1],[-1,1]]
    def solve(x,y):
        for i in range(8):
            for direction in directions:
                nx = x + direction[0] * i
                ny = y + direction[1] * i
                if 1<= nx <= 8 and 1<= ny <= 8:
                    visited.add((nx,ny))

    for bishop in bishops:
        x = alpha[bishop[0]]
        y = int(bishop[1])
        solve(x,y)

    return 64 - len(visited)


bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")