n = int(input())
count = 0
    
while n > 0: 
    if n % 5 == 0:
        count += n // 5
        break
    # 5로 나누어 떨어지지 앟는 경우엔 나누어 떨어질 때까지 2씩 빼주기
    else:    
        n -= 2
        count += 1
        
if n < 0 :
    print(-1)   
else:
    print(count)

    
        