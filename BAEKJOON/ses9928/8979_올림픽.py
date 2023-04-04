


n,k = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:(-x[1],-x[2],-x[3]))
rank = dict()
cnt = 1
rank[arr[0][0]] = 1

for i in range(n-1):
    if arr[i][1] == arr[i+1][1] and arr[i][2] == arr[i+1][2] and arr[i][3] == arr[i+1][3]:
        cnt += 1
        rank[arr[i+1][0]] = rank[arr[i][0]]
    else:
        rank.setdefault(arr[i+1][0],rank[arr[i][0]]+cnt)
        cnt = 1

print(rank[k])