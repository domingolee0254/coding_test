###########################################################################################
# so1 - cnt 잘 관리하기, recursion, index 잘 생각하기(몇부터 몇까지 돌아야 하는지 등등)
###########################################################################################

import sys

def dfs(x, y, dx, dy, visited_map):
    cnt = 1
    visited_map[x][y] = True
    for dir_idx in range(4):
        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]
        
        if (0 <= nx < N) and (0 <= ny < M):
            if og_map[nx][ny] == 1 and not visited_map[nx][ny]:
                cnt += dfs(nx, ny, dx, dy, visited_map)
    return cnt

def main(N, M, K, og_map):
    visited_map = [[False] * M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    max_size = 0
    
    for row in range(N):
        for col in range(M):
            if og_map[row][col] == 1 and not visited_map[row][col]:
                current_size = dfs(row, col, dx, dy, visited_map)
                max_size = max(max_size, current_size)
    return max_size

if __name__=="__main__":
    sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    N, M, K = map(int, input().strip().split())
    og_map = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        tmp_r, tmp_c = map(int, input().strip().split())
        og_map[tmp_r-1][tmp_c-1] = 1
        
    ret = main(N, M, K, og_map)
    print(ret)
    
###################################################################
# 실패
###################################################################

# import sys

# def dfs(x, y , dx, dy,visited_map, cnt):

#     for dir_idx in range(4):
#         nx = x + dx[dir_idx]
#         ny = y + dy[dir_idx]
        
#         if (0 < nx <= N) and (0 < ny <= M) and og_map[nx][ny] == 1: # if not 0 > nx or nx > N or 0 > ny or ny > M
#             visited_map[nx][ny] = True
#             cnt += 1
#             dfs(nx, ny, dx, dy,visited_map, cnt)
       
# def main(N, M, K, og_map):
#     visited_map = [[False]*(M+1) for _ in range(N+1)]
    
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
    
#     for row in range(N):
#         for col in range(M):
#             if og_map[row][col] == 1:
#                 x = row
#                 y = col
#                 cnt = 0
#                 dfs(x, y , dx, dy,visited_map, cnt)
                

# if __name__=="__main__":
#     sys.setrecursionlimit(10 ** 6)
#     input = sys.stdin.readline
#     N, M, K = map(int, input().strip().split())
#     og_map = [[0]*(M+1) for _ in range(N+1)]
    
#     for _ in range(K):
#         tmp_r, tmp_c = map(int, input().strip().split())
#         og_map[tmp_r][tmp_c] = 1
        
#     ret = main(N, M, K, og_map)