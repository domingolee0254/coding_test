import sys

def dfs(c):
    ans_dfs.append(c) # 현재 방문 노드 추가
    v_dfs[c] = 1 #방문 표시
    
    for n in adj[c]:
        if v_dfs[n] == 0: # 방문하지 않은 노드인 경우
            dfs(n)
            
def bfs(s):
    q = [] #필요한 q,v[], 변수 생성
    
    q.append(s) # q에 초기 데이터(들) 삽입
    ans_bfs.append(s)
    v_bfs[s] = 1
    
    while q:
        c = q.pop(0)
        for n in adj[c]:
            if v_bfs[n] == 0: #방문하지 않은 노드 => 큐 삽입
                q.append(n)
                ans_bfs.append(n)
                v_bfs[n] = 1

def main(N:int, V:int, adj:list)->int:
    
    # 오름차순 정렬
    for i in range(1, N+1):
        adj[i].sort()
    
    global ans_dfs, ans_bfs, v_dfs, v_bfs
    ans_dfs = []
    v_dfs = [0]*(N+1)
    dfs(V)
    
    ans_bfs = []
    v_bfs = [0]*(N+1)
    bfs(V)
    
    return ans_dfs, ans_bfs


if __name__ == '__main__': 
    input = sys.stdin.readline
    N, M, V = map(int, input().strip().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s) # 양방향
    
    ret1, ret2 = main(N, V, adj)
    print(*ret1)    
    print(*ret2)    