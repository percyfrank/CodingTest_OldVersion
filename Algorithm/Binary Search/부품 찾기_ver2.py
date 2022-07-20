'''
* 계수 정렬로 풀기

* 입력 받을 정수 N만큼의 리스트 선언부터 시작
'''


n = int(input())
array = [0] * 1000001
machines = list(map(int,input().split()))

for machine in machines:
    array[machine] = 1 

m = int(input())
item_list = list(map(int,input().split()))


for item in item_list:
    if array[item] == 1:
        print("yes", end = " ")
    else:
        print("no", end = " ")

