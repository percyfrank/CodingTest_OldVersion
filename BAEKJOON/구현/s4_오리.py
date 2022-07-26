
sounds = input()                    # 울음소리 입력받기
ducks = ['q','u','a','c','k']       # 오리 울음소리 패턴
visited = [False] * len(sounds) 
count = 0                           # 오리의 수
idx = 0                             # ducks 인덱스 저장

   
for i in range(len(sounds)):  
    if sounds[i] == 'q' and not visited[i]: # 시작 지점       
        cycle = True                        # 한 오리의 연속된 울음소리 저장
        for j in range(len(sounds)):
            if not visited[j] and ducks[idx] == sounds[j]: # 입력받은 녹음 소리가 울음소리 패턴과 일치할 경우
                visited[j] = True            # 방문한 울음소리는 True로 변경
                if sounds[j] == 'k':         # 울음소리 마지막                   
                    if cycle:                # 다른 오리의 울음 소리이면 if문 들어가서 오리의 수 +1
                        count += 1 
                        cycle = False         
                    idx = 0                  # 같은 오리의 울음 소리이면 울음소리 초기화
                    continue                 # 다음 울음소리로 넘어감
                idx += 1
                               
if len(sounds) % 5 != 0 or count == 0 or not all(visited):
    print(-1)
else:
    print(count)        
                
        

