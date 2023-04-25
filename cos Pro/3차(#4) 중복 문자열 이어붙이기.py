def solution(s1, s2):
    answer = float('inf')
    length = min(len(s1),len(s2))
    for i in range(length):
        if s1[length-(i+1):] == s2[:i+1]:
            answer = min(answer,len(s2)+i)
        if s2[length-(i+1):] == s1[:i+1]:
            answer = min(answer,len(s1)+i)
    return answer


s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")