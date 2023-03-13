n = int(input())
datas = map(int,input().split())
count = 0

def is_prime_num(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

for data in datas:
    if is_prime_num(data):
        count += 1
        
print(count)