import sys
from collections import deque

input = sys.stdin.readline
comps = int(input().strip())
conns = int(input().strip())
pair_list = [[] for _ in range((comps + 1))]
for i in range(conns):
    s, e = map(int, input().strip().split())
    pair_list[s].append(e)
    pair_list[e].append(s)

def bfs():
    queue = deque([1])  # 1번 컴퓨터에서 시작
    visited = [False] * (comps + 1)
    visited[1] = True  # 1번 컴퓨터는 이미 방문한 것으로 표시
    cnt = 0  # 1번 컴퓨터를 제외한 감염된 컴퓨터 수

    while queue:
        cur_comp = queue.popleft()
        for neighbor in pair_list[cur_comp]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                cnt += 1  # 1번 컴퓨터를 제외한 감염된 컴퓨터 수

    return cnt

print(bfs())