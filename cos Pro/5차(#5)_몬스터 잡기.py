def solution(enemies, armies):
    answer = 0
    e = len(enemies)
    a = len(armies)

    if a > e:
        armies.sort(reverse=True)
        armies = armies[:e]
    else:
        enemies.sort()
        enemies = enemies[:a]

    for i in range(min(a,e)):
        if armies[i] >= enemies[i]:
            answer += 1
    return answer

enemies1 = [1, 4, 3]
armies1 = [1, 3]
ret1 = solution(enemies1, armies1)

print("solution 함수의 반환 값은", ret1, "입니다.")

enemies2 = [1, 1, 1]
armies2 = [1, 2, 3, 4]
ret2 = solution(enemies2, armies2)