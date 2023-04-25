def solution(phrases, second):
    answer = ''

    second = second % 28
    if 1<= second <= 14:
        answer = "_" * (14-second) + phrases[:second]
    else:
        answer = phrases[second%14:] + "_" * (14-(second%14))
    return answer


phrases = "happy-birthday"
second = 3
ret = solution(phrases, second)

print("solution 함수의 반환 값은", ret, "입니다.")