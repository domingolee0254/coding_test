import sys

def dfs(x, y, M, N, visited_map, og_cab_map, dx, dy):
    stack = [(x, y)]
    visited_map[y][x] = True  # y, x 순서로 변경
    while stack:
        curr_x, curr_y = stack.pop()
        for dir_idx in range(4):
            nx = curr_x + dx[dir_idx]
            ny = curr_y + dy[dir_idx]
            if 0 <= nx < M and 0 <= ny < N:
                if og_cab_map[ny][nx] == 1 and not visited_map[ny][nx]:
                    visited_map[ny][nx] = True
                    stack.append((nx, ny))

def main(M, N, cabbage_locs):
    visited_map = [[False]*M for _ in range(N)]  # M열 N행
    og_cab_map = [[0]*M for _ in range(N)]  # M열 N행

    for x, y in cabbage_locs:
        og_cab_map[y][x] = 1  # y, x 순서로 변경

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    num_worms = 0
    for y in range(N):  # N 행
        for x in range(M):  # M 열
            if og_cab_map[y][x] == 1 and not visited_map[y][x]:
                num_worms += 1
                dfs(x, y, M, N, visited_map, og_cab_map, dx, dy)

    return num_worms

if __name__=="__main__":
    input = sys.stdin.readline
    T = int(input().strip())
    rets = []
    for _ in range(T):
        M, N, K = map(int, input().strip().split())
        cabbage_locs = [list(map(int, input().strip().split())) for _ in range(K)]
        ret = main(M, N, K, cabbage_locs)
        rets.append(ret)
    
    for ret in rets:
        print(ret)
#################################################################################
# 실패 - M, N 헷갈림, dfs 내부를 어떻게 처리할 지
#################################################################################
# import sys
# from collections import deque


# def dfs(curr_x, curr_y):
            
#     # 4방향 이동 함수    
#     for dir_idx in range(4):
#         nx = curr_x + dx[dir_idx]
#         ny = curr_y + dy[dir_idx]
#         # 방향 이동 가능 조건 - og_map 배열 안에 있어야 함
#         if 0 < nx and nx < M and 0 < ny and ny < N:
#             dfs(nx, ny)
        
#         else:
#             break
#     return 0
    
# def main(M:int, N:int, K:int, cabbage_roc:list) -> list:
#     visited_map = [[-1]*M for _ in range(N)]
#     og_cab_map = [[0]*M for _ in range(N)]

#     # draw cabbage original map
#     for tmp_cord in cabbage_roc:   # [0,0]
#         og_cab_map[tmp_cord[0]][tmp_cord[1]] = 1 
    
#     curr_cord = cabbage_roc.popleft()
    
#     # direction init # 상하좌우
#     dx = [0, 0, -1, 1] 
#     dy = [-1, 1, 0, 0]
    
#     num_worm = 0
#     if og_cab_map[curr_cord[0]][curr_cord[1]] == 1 and visited_map[curr_cord[0]][curr_cord[1]] == -1:
#         num_worm += 1
        
        
#         dfs(x, y)

#     else:
#         pass
    
#     return curr_roc
    
    
    
# if __name__=="__main__":
#     input = sys.stdin.readline
#     T = int(input().strip())
#     for _ in range(T):
#         M, N, K = map(int, input().strip().split())
#         cabbage_roc = [list(map(int, input().strip().split())) for _ in range(K)]

#         ret = main(M, N, K, cabbage_roc)

#         print(ret)
