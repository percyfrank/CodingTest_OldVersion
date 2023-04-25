import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(a, b):

    nums = set()
    for num in range(1, b+1):
        if isPrime(num):
            if a <= num**2 <= b:
                nums.add(num**2)
            if a <= num**3 <= b:
                nums.add(num**3)

    return len(nums)

a =  6
b =  30
ret = solution(a, b)

print("solution 함수의 반환 값은", ret, "입니다.")