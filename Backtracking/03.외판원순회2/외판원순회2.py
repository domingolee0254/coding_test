###############################################################
# sol 1
###############################################################
import sys

def dfs_bt(start, next, weight, visited):
    global min_w
    # 모든 도시를 방문한 경우
    if sum(visited) == N:
        # 출발 도시로 돌아갈 수 있는지 확인하고, 가능하면 최소 비용 갱신
        if W[next][start]:
            min_w = min(min_w, weight + W[next][start])
        return

    # 가능한 모든 도시를 방문
    for i in range(N):
        # 아직 방문하지 않은 도시이며 경로가 존재하고, 현재 비용이 최소 비용보다 작은 경우에만 탐색
        if visited[i] == 0 and W[next][i] != 0 and weight + W[next][i] < min_w:
            visited[i] = 1 # 방문
            dfs_bt(start, i, weight + W[next][i], visited)
            visited[i] = 0  # 방문 상태를 되돌림


def main(N, W):
    global min_w
    min_w = sys.maxsize
    visited = [0]*N
    # 각 도시를 시작점으로 설정하고 DFS 탐색
    for city_idx in range(N):
        visited[city_idx] = 1
        dfs_bt(city_idx, city_idx, 0, visited)
        visited[city_idx] = 0  # 다음 시작 도시를 위해 방문 상태 초기화
    return min_w

if __name__=="__main__":
    input = sys.stdin.readline
    global N, W
    N = int(input().strip())
    W = [list(map(int, input().strip().split())) for _ in range(N)]
    ret = main(N, W)
    print(ret)
    
###############################################################
# GPT code
###############################################################
# import sys

# def dfs_bt(current, weight, visited, count):
#     global min_cost, N, W

#     # 모든 도시를 방문했고, 시작점으로 돌아가는 경로가 존재하는 경우
#     if count == N:
#         if W[current][0] > 0:
#             min_cost = min(min_cost, weight + W[current][0])
#         return

#     # 다른 도시 탐색
#     for next in range(N):
#         if not visited[next] and W[current][next] > 0:
#             if weight + W[current][next] < min_cost:  # 가지치기: 이미 찾은 최소비용보다 크면 탐색 중지
#                 visited[next] = True
#                 dfs_bt(next, weight + W[current][next], visited, count + 1)
#                 visited[next] = False  # 재귀 호출 후 방문 상태를 되돌림

# def main(N, W):
#     global min_cost
#     min_cost = float('inf')
#     visited = [False] * N
#     visited[0] = True  # 0번 도시에서 시작
#     dfs_bt(0, 0, visited, 1)
#     return min_cost


# if __name__=="__main__":
#     input = sys.stdin.readline
#     global N, W
#     N = int(input().strip())
#     W = [list(map(int, input().strip().split())) for _ in range(N)]
#     ret = main(N, W)
#     print(ret)

    
###############################################################
# fail ans = 95
###############################################################
# import sys

# def dfs(n:int, w_lst:list) -> int:
    
#     if n == N:
#         ans.append(w_lst)
#         return

#     for i in range(N):
#         for j in range(N):
#             if i == j:
#                 continue
#             else:
#                 if vst[i] == 0 and W[i][j] != 0:
#                     vst[i] = 1
#                     w_lst.append(W[i][j])
#                     dfs(n+1, w_lst)
#                     vst[i] = 0

# def main(N:int, W:list) -> int:
#     global ans, vst, w_lst
    
#     ans = []
#     vst = [0]*N
#     tmp_list = []
#     dfs(0, [])
    
#     for ele in ans:
#         tmp_list.append(sum(ele))
    
#     sum_min_w = min(tmp_list)
    
#     return sum_min_w

# if __name__=="__main__":
#     input = sys.stdin.readline
#     global N, W
#     N = int(input().strip())
#     W = [list(map(int, input().strip().split())) for _ in range(N)]
#     ret = main(N, W)
#     print(ret)
    