from itertools import permutations

def solution(card, n):

    card = list(map(str,card))
    arr = list(map(''.join,permutations(card,len(card))))
    arr = list(map(int,set(arr)))
    arr.sort()

    answer = 0
    for i,data in enumerate(arr):
        if data == n:
            answer = i+1
            break

    if answer == 0:
        return -1
    else:
        return answer

card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
