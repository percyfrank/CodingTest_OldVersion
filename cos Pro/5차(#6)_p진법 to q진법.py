def to10(n,exp):
    length = len(n)
    num = 0
    for i in range(length):
        num += exp**i * int(n[length-i-1])

    return num

def solution(s1, s2, p, q):
    answer = ''

    s1 = to10(s1,p)
    s2 = to10(s2,p)

    total = s1 + s2
    regex = "0123456789"

    while total > 0:
        a,b = divmod(total,q)
        answer = regex[b] + answer
        total = a

    return answer

s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

print("solution 함수의 반환 값은", ret, "입니다.")