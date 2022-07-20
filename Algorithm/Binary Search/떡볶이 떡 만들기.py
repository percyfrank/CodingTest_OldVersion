def binary_search(target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for array in arrays:
            # 떡 높이가 절단기 높이보다 작으면 넘어감
            if array < mid:
                pass
            else:
                total += array - mid
        # 떡의 양이 부족한 경우(왼쪽 부분 탐색)
        if total < target:
            end = mid - 1
        # 떡의 양이 충분한 경우(오른쪽 부분 탐색)
        else:
            result = mid     # M만큼의 떡을 가져가기 위한 절단기 높이의 최솟값
            start = mid + 1
    return result

n,m = map(int,input().split())
arrays = list(map(int,input().split()))

print(binary_search(m, 0, max(arrays)))    
