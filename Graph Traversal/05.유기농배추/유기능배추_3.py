import sys
sys.setrecursionlimit(10 ** 6)

def dfs(y, x, cnt):
    global visited, directions

    for dir_idx in directions:
        ny, nx = y + dir_idx[0], x + dir_idx[1]

        if (0<=ny<N) and (0<=nx<M) and og_map[ny][nx] == 1 and not visited[ny][nx]:            
            visited[ny][nx] = True
            dfs(ny, nx, cnt)

    return cnt

def main():
    global visited, directions

    visited = [[False] * M for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    worm_list = []

    for i in range(N):
        for j in range(M):
            if og_map[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                worm_list.append(dfs(i, j, 1))
    return sum(worm_list)


input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().strip().split())
    og_map = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().strip().split())
        og_map[Y][X] = 1
    ret = main()
    print(ret)