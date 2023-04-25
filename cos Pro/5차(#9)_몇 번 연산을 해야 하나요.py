def solution(number, target):
    answer = 0

    tmp = [0] * 3
    MIN = float('inf')

    while True:
        idx = 0
        tmp[0] = number + 1
        tmp[1] = number - 1
        tmp[2] = number * 2
        for cal in range(3):
            if tmp[cal] == target:
                idx = cal
                break
            if abs(tmp[cal]-target) < MIN:
                idx = cal
                MIN = abs(tmp[cal]-target)
        number = tmp[idx]
        answer += 1
        if number == target:
            break
    return answer

number1 = 5
target1 = 9
ret1 = solution(number1, target1)

print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

print("solution 함수의 반환 값은", ret2, "입니다.")