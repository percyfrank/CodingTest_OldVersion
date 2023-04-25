
from itertools import combinations

def solution(arr, K):
    answer = 0
    nums = list(combinations(arr,3))
    for num in nums:
        if sum(num) % K == 0:
            answer += 1
    return answer


arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

print("solution 함수의 반환 값은", ret, "입니다.")