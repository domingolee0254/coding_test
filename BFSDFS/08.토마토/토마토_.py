import sys
from collections import deque

def bfs(tomato_box, N, M):
    global visited, ans, dx, dy
    
    q = deque()
    
    for r in range(N):
        for c in range(M):
            if tomato_box[r][c] == 1:
                q.append((r, c))
                visited[r][c] = 1
    
    ans = -1  # 일수를 -1로 초기화 (마지막에 하루 더하기 때문)
    
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dir_idx in range(4):
                nx = c + dx[dir_idx]
                ny = r + dy[dir_idx]
                if 0 <= ny < N and 0 <= nx < M and tomato_box[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    tomato_box[ny][nx] = 1
                    q.append((ny, nx))
        ans += 1

    for r in range(N):
        for c in range(M):
            if tomato_box[r][c] == 0:
                return -1
    
    return ans

def main(N, M, tomato_box):
    global visited, dx, dy
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited = [[0] * M for _ in range(N)]
    result = bfs(tomato_box, N, M)
    return result

if __name__ == "__main__":
    input = sys.stdin.readline
    M, N = map(int, input().strip().split())
    tomato_box = [list(map(int, input().strip().split())) for _ in range(N)]
    ret = main(N, M, tomato_box)
    print(ret)