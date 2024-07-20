# key idea1 : 왜 bfs일까 - 가중치 없는 최단경로는 bfs
# key idea2: visited를 3차원 배열로 만들어서 벽 부수기 전/후 둘다 저장
# 애초에 왜 3차원 배열을 해야하지? 어떻게 3차원 배열을 해야겠다는 생각을 하지? 그 생각의 시작점이 뭐지?
import sys
from collections import deque


def bfs():
    global visited_map, dx, dy

    q = deque()
    # 초기값 삽입
    q.append((0,0,0))
    visited_map[0][0][0] = 1
    
    while q:
        x, y, crashed = q.popleft()
          
        # 탈출, 종료 조건 확인
        if x == M-1 and y == N-1:
            return visited_map[y][x][crashed]
        
        # 방향 돌리기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # nx, ny가 map 안에 있을 때
            if (0 <= nx < M) and (0 <= ny < N):
                # 1. 갈수 있는 경우(벽 아닐 때)
                #   1.1 (갈 수 있는 데 && 안가본 곳) -> 가고 업데이트
                #   1.2 (갈 수 있는 데 && 가본 곳) -> pass  
                if og_map[ny][nx] == 0 and visited_map[ny][nx][crashed] == 0: # 1.1인 경우 
                    visited_map[ny][nx][crashed] = visited_map[y][x][crashed] + 1 # 어려움
                    # visited_map[ny][nx][0] = visited_map[y][x][0] + 1 이면 왜 안되는 거야
                    # crashed 자체가 인덱스이고, 벽을 깨졌음을 말하는 거임. 이미 한번 벽이 깨지면 인덱스는 계속 1인 거임
                    # N이0일 때 [[1,3], [0,2], [0,3], [0,4]]는 각 [x,x] 들의 1번 째 값들만 커지는 게 벽이 깨졌음을 의미함, 벽이 깨졌기 때문에 1번째 인덱스만 값을 키워주는 거임
                    # 1번째 인덱스의 value들은 이동 경로의 수임.(1번 벽을 깼을 때 이동한 횟수를 의미)
                    q.append((nx, ny, crashed))
                # 2. 갈수 없는 경우
                #   2.1. 벽일 때 && 한번도 안깸 && 안가본 곳-> 가고 업데이트
                #   2.2. 벽일 때 && 한번도 안깸 && 가본 곳-> 이런 경우가 아예 없지, 벽인데 간 경우는 이미 깨본곳인데
                #   2.3. 벽일 때 && 한번 깸 -> pass
                elif og_map[ny][nx] == 1 and visited_map[ny][nx][crashed] == 0: # 2
                    if crashed == 0:
                        visited_map[ny][nx][1] = visited_map[y][x][crashed] + 1
                        q.append((nx, ny, 1)) # q.append((ny, nx, 1)) 로 하면 앞 pop에서도 고쳐주기
                    elif crashed == 1:  # else로 하면 안될듯(2번 이상 깨지는 애들이 else에 들어가니까)
                        continue
                    else:
                        continue
    return -1 # 예외 처리


def main(N:int, M:int, og_map:list) -> int:
    global visited_map, dx, dy
    
    # 변수들 초기화
    visited_map = [[[0,0] for _ in range(M)] for _ in range(N)]   # 이거 몰라, [0,0]이 뭘 나타내는 거야 => 앞에거는 벽 안깬경우, 뒤는 깬경우

    # 상 하 좌 우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    return bfs() 

if __name__=="__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    og_map = [list(map(int, input().strip())) for _ in range(N)] # 그냥 int(input().strip())하면 문자열 맨앞의 0 사라짐
    ret = main(N, M, og_map)
    print(ret)

#visited_map = [[[0,0] for _ in range(M)] for _ in range(N)]   # 이거 몰라, [0,0]이 뭘 나타내는 거야 => 앞에거는 벽 안깬경우, 뒤는 깬경우
    # [r=y, c=x, 0/1 벽깼는지 아닌지]
    # print(visited_map)
    # print(len(visited_map)) # 6
    # print(len(visited_map[0]))  # 4
    # print(len(visited_map[0][0]))  # 2
    # print(visited_map) # [[[0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0]]


#############################################################################################################
# sol1) bfs -> 벽 통과 못한다고 했을 때, 일반적인 bfs(뭐가 다른지 비교해보려고 만듦)
#############################################################################################################
# 애초에 왜 3차원 배열을 해야하지? 어떻게 3차원 배열을 해야겠다는 생각을 하지? 그 생각의 시작점이 뭐지?
# import sys
# from collections import deque


# def main(N, M, maze):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]

#     visited = [[-1] * M for _ in range(N)]  # 방문 여부 및 최단 거리를 저장할 배열
#     visited[0][0] = 1  # 시작점 (0, 0)의 최단 거리를 1로 초기화
#     queue = deque([(0, 0)])  # 시작점 (0, 0)을 큐에 넣음

#     while queue:
#         x, y = queue.popleft()

#         if x == N - 1 and y == M - 1:  # 목적지에 도착한 경우
#             return visited[x][y]

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < N and 0 <= ny < M:
#                 if maze[nx][ny] == 0 and visited[nx][ny] == -1:
#                     visited[nx][ny] = visited[x][y] + 1
#                     queue.append((nx, ny))
    
#     return -1  # 도착지에 도달할 수 없는 경우

# if __name__=="__main__":
#     input = sys.stdin.readline
#     N, M = map(int, input().strip().split())
#     og_map = [list(map(int, input().strip())) for _ in range(N)] # 그냥 int(input().strip())하면 문자열 맨앞의 0 사라짐
#     ret = main(N, M, og_map)
#     print(ret)
    
#############################################################################################################
# sol2) dfs -> 실패, 인덱스 에러남
#############################################################################################################

# # key idea : dfs의 if문을 만들어서 -> 1. 1을 부순다 -> 부수면 cnt+1/ 2. 0을 탄다(cnt=1이면 계속 이것만 수행하도록)
# import sys
# def dfs(x, y):
#     visited_map[x][y] = True
#     global one_cnt
#     one_cnt = 0
    
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
    
#     for dir_idx in range(4):
#        nx = x + dx[dir_idx]
#        ny = y + dy[dir_idx]
       
#        if (0 <= nx < N) and (0 <= nx < M):
#             if og_map[nx][ny] == 1 and one_cnt == 0 and visited_map[nx][ny]:
#                 # og_map[nx][ny] = 0
#                 dfs(nx, ny)
#                 pass # 부수고 진행
                
#             elif og_map[nx][ny] == 1 and one_cnt == 1:
#                 return False
            
#             elif og_map[nx][ny] == 0 and not visited_map[nx][ny]:
#                dfs(nx, ny)
    
# def main(N:int, M:int, og_map:list):
    
#     global visited_map
#     #initalize
#     visited_map = [[False]*M for _ in range(N)]
    
#     print(og_map)
#     for r in range(N): # N = row
#         for c in range(M): # N = col
#             if og_map[r][c] == 0 and not visited_map[r][c]: # False가 아니면 진행, 즉 안가본 곳이면 진행
#                 dfs(r, c)
    
# if __name__=="__main__":
#     sys.setrecursionlimit(10 ** 6)
#     input = sys.stdin.readline
#     N, M = map(int, input().strip().split())
    
#     global og_map
#     # [[0, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]] 리스트-맵-리스트 한거는 이렇게 만들어주기 위함 
#     og_map = [list(map(int, list(input().strip().split()[0]))) for _ in range(N)] # list()를 넣어야 'hello'가 ['h', 'e','l', 'l', 'o']
        
#     ret = main(N, M, og_map)
    
    