import sys
sys.setrecursionlimit(10**8) #

def dfs(x, y):
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    if x == M-1 and y == N-1:
        return 1
    
    if vst[x][y] != -1:
        return vst[x][y]
        
    cnt = 0
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < M and 0 <= ny < N:  # 범위 조건
            if arr[nx][ny] < arr[x][y]:
                cnt += dfs(nx, ny)  
    
    vst[x][y] = cnt
    return cnt

def main():
    global M, N, arr, vst #
    M, N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    vst = [[-1 for _ in range(N)] for _ in range(M)]
    return int(dfs(0, 0))

if __name__ == "__main__":
    # 전역 변수 선언
    M, N = 0, 0
    arr = []
    vst = []
    ret = main()
    print(ret)
