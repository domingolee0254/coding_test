# 2636번 

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    global directions, visited

    # 외부 공기를 탐색하기 위한 큐
    air_queue = deque([(0, 0)])
    # 녹을 치즈를 저장하기 위한 큐
    melt_queue = deque()

    # BFS를 이용해 외부 공기와 접촉한 치즈를 찾음
    while air_queue:
        cy, cx = air_queue.popleft()
        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            if (0 <= ny < N) and (0 <= nx < M) and not visited[ny][nx]:
                visited[ny][nx] = True
                if grid[ny][nx] == 0:
                    air_queue.append((ny, nx))
                elif grid[ny][nx] == 1:
                    melt_queue.append((ny, nx))

    # 녹을 치즈를 모두 공기로 변환
    for y, x in melt_queue:
        grid[y][x] = 0
    
    # 녹인 치즈의 개수를 반환
    return len(melt_queue)

def main():
    global directions, visited

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 전체 치즈의 초기 개수를 세기 위한 변수
    og_num_chz = 0
    time = 1

    # 치즈의 초기 개수를 셈
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                og_num_chz += 1

    # 치즈가 모두 녹을 때까지 반복
    while True:
        visited = [[False] * M for _ in range(N)]
        # 한 시간 동안 녹은 치즈의 개수를 구함
        num_melted_chz = bfs()
        # 전체 치즈 개수에서 녹은 치즈 개수를 뺌
        og_num_chz -= num_melted_chz
        # 치즈가 모두 녹았으면 시간을 반환
        if og_num_chz == 0:
            return time, num_melted_chz
        time += 1

ret1, ret2 = main()
print(ret1)
print(ret2)
