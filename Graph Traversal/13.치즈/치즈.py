# 2638번 

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(N)]

def bfs(visited):
    
    air_queue = deque([(0, 0)])
    melt_queue = deque()
    
    while air_queue:
        cy, cx = air_queue.popleft()
        for dy, dx in directions:
            ny, nx = cy + dy, cx + dx
            if (0<=ny<N) and (0<=nx<M):
                if grid[ny][nx] == 0 and visited[ny][nx] == 0:  # 공기를 만난 경우
                    air_queue.append((ny, nx))
                    visited[ny][nx] = 1

                elif grid[ny][nx] == 1:  # 치즈를 만난 경우
                    visited[ny][nx] += 1  # 접촉한 면적 증가
                    if visited[ny][nx] >= 2:  # 두 면 이상 접촉하면 녹음
                        melt_queue.append((ny, nx))
                  
    for y, x in melt_queue:
        grid[y][x] = 0

    return len(melt_queue) > 0  # 녹은 치즈가 있으면 True, 없으면 False

def main():
    global directions

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    time = 0
    while True:
        visited = [[0]*M for _ in range(N)]
        air_cnt = bfs(visited)
        if not air_cnt:  # 치즈가 더 이상 녹지 않으면 종료
            break
        time += 1
    
    return time

ret = main()
print(ret)