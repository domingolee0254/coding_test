def count_speeding_violations(speeds, positions, times):
    count = 0

    for i in range(1, len(positions)):
        # 구간 거리 및 시간 계산
        distance = positions[i] - positions[i-1]
        time_taken = times[i] - times[i-1]

        # 속도 계산 (속력 = 거리 / 시간)
        if time_taken != 0:
            speed = distance / time_taken
        else:
            speed = float('inf') # 걸린 시간이 0 이면 무한대의 속도라고 가정
        
        # 제한속도 초과 여부 확인
        if speed > speeds[i-1]:
            count += 1

    return count

speeds = [50, 60, 70]
positions = [10, 50, 90]
times = [1, 2, 4]

# 함수 호출 및 결과 출력
violations = count_speeding_violations(speeds, positions, times)
print(violations)  # 출력: 0