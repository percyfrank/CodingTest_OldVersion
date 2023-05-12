n = int(input())
arr = list(map(int,input().split()))
total = int(input())

tmp = 0
answer = 0
start = total // n
end = max(arr)

while start <= end:
    mid = (start+end) // 2
    tmp = 0
    for data in arr:
        if data < mid:
            tmp += data
        else:
            tmp += mid
    if tmp > total:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)
