


def solution(arr):
    answer = 0
    idx = 0
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            answer = max(answer,i-idx+1)
            idx = i+1
    return answer


arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")