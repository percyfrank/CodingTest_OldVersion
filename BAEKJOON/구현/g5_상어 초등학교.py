n = int(input())

students = []
for _ in range(n**2):
    students.append(list(map(int,input().split())))

# 하 상 좌 우
dr = [1,-1,0,0]
dc = [0,0,-1,1]

seat = [[0]*n for _ in range(n)]


for i in range(n**2):
    student = students[i]
    
    temp = []
    for r in range(n):
        for c in range(n):
            if seat[r][c] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if seat[nr][nc] in student[1:]:
                            like += 1
                        if seat[nr][nc] == 0:
                            blank += 1
                temp.append([like,blank,r,c])
    temp.sort(key = lambda x: (-x[0],-x[1],x[2],x[3]))
    seat[temp[0][2]][temp[0][3]] = student[0]


students.sort()



cnt = 0
ans = 0
for i in range(n):
    for j in range(n):
        m = seat[i][j] 
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if seat[nr][nc] in students[m-1][1:]:
                    cnt += 1
        if cnt == 0:
            ans += 0
        else:
            ans += 10**(cnt-1)
        cnt = 0 

print(ans)