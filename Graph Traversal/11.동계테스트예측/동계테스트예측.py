import sys
from collections import deque

# 외부 공기 접촉 상태를 계산하는 함수
def get_air_contact(N, M, grid):
    global directions, visited

    queue = deque([(0, 0)])  # BFS를 위한 큐 초기화, 시작점은 (0, 0)
    contact = [[0] * M for _ in range(N)]  # 외부 공기와의 접촉 횟수를 저장할 배열

    # BFS를 통해 외부 공기 영역 탐색
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (0 <= ny < N) and (0 <= nx < M) and not visited[ny][nx]:
                if grid[ny][nx] == 0:  # 외부 공기인 경우
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                elif grid[ny][nx] == 1:  # 얼음인 경우 접촉 횟수 증가
                    contact[ny][nx] += 1
    return contact

# 얼음을 녹이는 함수
def melt_ice(grid, contact, N, M):

    melted = False  # 얼음이 녹았는지 여부를 추적
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and contact[i][j] >= 2:  # 외부 공기와 2변 이상 접촉한 얼음
                grid[i][j] = 0  # 얼음을 녹임
                melted = True  # 녹은 얼음이 있음을 표시
    return melted

# 전체 시뮬레이션을 수행하는 함수
def main(N, M, grid):
    global directions, visited

    time = 0  # 시간을 초기화
    # 상하좌우 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        visited = [[False] * M for _ in range(N)]  # 방문 여부를 저장할 배열
        visited[0][0] = True  # 시작점을 방문으로 표시
        contact = get_air_contact(N, M, grid)  # 외부 공기 접촉 상태 갱신
        if not melt_ice(grid, contact, N, M):  # 얼음이 녹지 않으면 루프 종료
            break
        time += 1  # 시간이 1 증가
    return time

input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(main(N, M, grid))