'''
* 선택 정렬 : 매번 가장 작은 것을 선택

* 시간 복잡도 : O(N^2)
'''

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_idx = i
    # 주어진 범위 내에서 가장 작은 원소의 인덱스 찾기
    for j in range(i+1,len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    # 가장 작은 원소를 맨 앞의 데이터랑 교체
    array[min_idx], array[i] = array[i], array[min_idx]
    
print(array)