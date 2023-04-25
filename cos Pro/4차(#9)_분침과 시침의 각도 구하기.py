def solution(hour, minute):
    answer = 30*hour - 6*minute

    return "{:.1f}".format(answer)

hour = 3
minute = 0
ret = solution(hour, minute)

print("solution 함수의 반환 값은", ret, "입니다.")