'''
* 팁 : 원래 주려했던 돈 - (등수 - 1)

* 손님의 순서를 적절히 바꾸었을 때, 받을 수 잇는 팁의 최댓값 출력
'''

import sys
input = sys.stdin.readline

n = int(input())

# 주려했던 돈
m = []
for i in range(n):
    m.append(int(input()))

m.sort(reverse=True)

# 주려했던 돈 - (받은 등수 - 1)
tip = 0
for i in range(n):
    if m[i] - (i+1 - 1) < 0:    # 팁이 음수라면 주지 않음
        pass
    else:
        tip += m[i] - (i+1 - 1)
    
print(tip)