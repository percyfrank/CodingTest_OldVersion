


def solution(num):
    num = str(num+1)
    num = num.replace("0","1")


    return num


num = 9949999;
ret = solution(num)

print("solution 함수의 반환 값은", ret, "입니다.")