'''
* 삽입 정렬 : 특정한 데이터를 적절한 위치에 삽입, 즉, 정렬되어 있는 데이터
              리스트에서 적절한 위치를 찾은 뒤에, 그 위치에 삽입됨

* 시간 복잡도 
  
  평균 : O(N^2) / 최선 : O(N)

* 거의 정렬되어 있는 상태의 데이터는 삽입 정렬 효율적
'''

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break 

    
print(array)