import sys

input = sys.stdin.readline
H, W = map(int, input().split())
heights = list(map(int, input().split()))

def main():
    if W == 0:
        return 0
    
    left_max = [0] * W
    right_max = [0] * W
    
    # 왼쪽 최대 높이 계산
    left_max[0] = heights[0]
    for i in range(1, W):
        left_max[i] = max(left_max[i - 1], heights[i])
    
    # 오른쪽 최대 높이 계산
    right_max[W - 1] = heights[W - 1]
    for i in range(W - 2, -1, -1): # start, stop, step
        right_max[i] = max(right_max[i + 1], heights[i])
    
    # 고이는 빗물의 양 계산
    total_water = 0
    for i in range(W):
        water_at_i = min(left_max[i], right_max[i]) - heights[i]
        if water_at_i > 0:
            total_water += water_at_i
    
    return total_water

ret = main()
print(ret)