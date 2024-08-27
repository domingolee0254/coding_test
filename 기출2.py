def max_trapezoid_area(coords):
    from collections import defaultdict

    # y값에 따라 x좌표를 저장할 딕셔너리
    y_to_x = defaultdict(list) # check 1

    # 각 (x, y) 좌표를 y를 키로 하여 딕셔너리에 저장
    for x, y in coords:
        y_to_x[y].append(x)
    
    max_area = 0
    max_coords = []  # 최대 넓이를 만드는 좌표를 저장할 리스트
    
    # 모든 y값 조합에 대해 사다리꼴을 구성
    y_values = sorted(y_to_x.keys())

    for i in range(len(y_values)):
        for j in range(i + 1, len(y_values)): # check 2
            y1, y2 = y_values[i], y_values[j]
            # y1, y2 그룹에서 최대와 최소 x값 찾기
            min_x1, max_x1 = min(y_to_x[y1]), max(y_to_x[y1])
            min_x2, max_x2 = min(y_to_x[y2]), max(y_to_x[y2])
            base1 = max_x1 - min_x1
            base2 = max_x2 - min_x2
            height = abs(y2 - y1)
            area_twice = (base1 + base2) * height
            if area_twice > max_area:
                max_area = area_twice
                max_coords = [(min_x1, y1), (max_x1, y1), (min_x2, y2), (max_x2, y2)]
                # max_area = max(max_area, area_twice) # check 3

    return max_area, max_coords

# 예시 입력
coords = [(0,0), (6,0), (1, 1), (3, 1), (4, 2), (6, 2), (2, 3), (5, 3), (2, 5), (5, 4), (5, 5)]

# 함수 호출 및 결과 출력
result, trapezoid_coords = max_trapezoid_area(coords)
print(f"Max area twice: {result}")
print(f"Coordinates: {trapezoid_coords}")
