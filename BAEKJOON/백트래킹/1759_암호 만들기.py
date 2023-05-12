

def solve(start):
    if len(answer) == l:
        vo = 0
        co = 0
        for data in answer:
            if data in vowels:
                vo += 1
                continue
            co += 1
        if vo >= 1 and co >= 2:
            print(''.join(answer))
        return

    for i in range(start,c):
        answer.append(arr[i])
        solve(i+1)
        answer.pop()


l,c = map(int,input().split())
arr = list(map(str,input().split()))
arr.sort()
vowels = ['a','e','i','o','u']
answer = []
solve(0)
