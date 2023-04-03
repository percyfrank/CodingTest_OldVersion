

def isTrianlge(arr):
    if arr[0] + arr[1] <= arr[2]:
        return True

def solve(arr):
    cnt = 0
    for i in range(2):
        if arr[i] == arr[i+1]:
            cnt += 1
    if cnt == 0:
        print('Scalene')
    elif cnt == 1:
        print("Isosceles")
    else:
        print("Equilateral")


while(True):
    arr = list(map(int,input().split()))
    arr.sort()
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    if isTrianlge(arr):
        print("Invalid")
        continue
    solve(arr)
