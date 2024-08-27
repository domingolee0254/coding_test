import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().strip().split())
box = [list(map(int, input().strip().split())) for _ in range(N)]

def bfs():
    global directions

    queue = deque()
    days = -1
    
    # 초기 상태에서 익은 토마토의 위치를 큐에 추가
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                queue.append((i, j))
    
    while queue:
        days += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                    box[nx][ny] = 1
                    queue.append((nx, ny))
    
    # 모든 토마토가 익었는지 확인
    for row in box:
        if 0 in row:
            return -1
    return days

def main():
    global directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return bfs()

ret = main()
print(ret)
