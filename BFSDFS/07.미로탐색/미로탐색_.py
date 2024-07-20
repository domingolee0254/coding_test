##################################################################
# sol 1) BFS
##################################################################
import sys
from collections import deque

def bfs(N:int, M:int, maze:list) -> int:
    global queue, distance
    
    # 방향 벡터: 상, 하, 좌, 우
    dx = [0, 0,- 1, 1]
    dy = [-1, 1, 0, 0]
    
    while queue:
        y, x = queue.popleft()
        # 네 방향으로 이동 시도
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # 미로 범위를 벗어나지 않게 체크하고, 이동할 수 있는 칸인지 확인
            if (0<=ny<N) and (0<=nx<M) and maze[ny][nx] == 1 and distance[ny][nx] == 0:
                queue.append((ny, nx))
                distance[ny][nx] = distance[y][x] + 1
                
                # 도착지점에 도달하면 결과 반환
                if ny == N-1 and nx == M-1:
                    return distance[ny][nx]
                
    return -1 # 도착 지점에 도달할 수 없는 경우
                
def main(N:int, M:int, maze:list) -> int:
    global queue, distance
    
    # 큐 초기화
    queue = deque([(0,0)])
    # 시작 위치의 거리 초기화
    distance = [[0]*M for _ in range(N)]
    distance[0][0] = 1
    
    # BFS를 수행하여 최단 경로 계산
    result = bfs(N, M, maze)

    return result

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    ret = main(N, M, maze)
    print(ret)

##################################################################
# sol 2) dfs_backtracking 이용 => 시간초과
##################################################################
# import sys
# sys.setrecursionlimit(10000)

# def dfs(x, y, maze, distance):
#     global ans
#     # 도착 지점에 도달하면 최소 거리를 갱신
#     if x == M - 1 and y == N - 1:
#         ans = min(ans, distance)
#         return
    
#     # 방향 벡터: 상, 하, 좌, 우
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         # 미로의 범위 내에 있고, 이동할 수 있는 칸이며, 방문하지 않은 칸인 경우
#         if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and maze[ny][nx] == 1:
#             visited[ny][nx] = True
#             dfs(nx, ny, maze, distance + 1)
#             visited[ny][nx] = False  # 백트래킹: 탐색이 끝난 후 방문 체크 해제

# def main(N, M, maze):
#     global ans, visited
    
#     # 최소 거리를 저장할 변수 초기화
#     ans = float('inf')
#     # 방문 여부를 기록할 2차원 리스트 초기화
#     visited = [[False] * M for _ in range(N)]
#     visited[0][0] = True
#     dfs(0, 0, maze, 1)
    
#     return ans

# if __name__ == "__main__":
#     input = sys.stdin.readline
#     N, M = map(int, input().strip().split())
#     maze = [list(map(int, input().strip())) for _ in range(N)]
#     ret = main(N, M, maze)
#     print(ret)

##################################################################
# sol 1) fail 일반 DFS 답이 안맞음
##################################################################

# import sys

# def dfs(x, y, maze):
#     global ans, visited
    
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if (0<=ny<N) and (0<=nx<M):
#             if visited[ny][nx] == False and maze[ny][nx] == 1:
#                 visited[ny][nx] = True
#                 ans += 1
#                 dfs(nx, ny, maze)


# def main(N:int, M:int, maze:list) -> list:
#     global ans, visited
    
#     ans = 0
#     visited = [[False]*M for _ in range(N)]
#     dfs(0, 0, maze)
    
#     return ans

# if __name__=="__main__":
#     input = sys.stdin.readline
#     N, M = map(int, input().strip().split())
#     maze = [list(map(int, input().strip())) for _ in range(N)]
#     ret = main(N, M, maze)
#     print(ret)