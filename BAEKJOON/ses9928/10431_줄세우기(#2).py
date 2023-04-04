

p = int(input())
arr = []
for i in range(p):
    arr = list(map(int,input().split()))
    arr = arr[1:]
    cnt = 0
    for j in range(20):
        for k in range(j+1,20):
            if arr[j] > arr[k]:
                cnt += 1
                arr[j], arr[k] = arr[k], arr[j]

    print(i+1,cnt)