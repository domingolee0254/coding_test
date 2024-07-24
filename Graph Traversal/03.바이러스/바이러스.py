import sys
from collections import deque

def bfs(adj, s=1):
    q = deque()
    q.append(s) # 처리 큐
    ans_bfs.append(s)
    visited[s] = 1
            
    while q:
        c = q.popleft()
        for n in adj[c]:
            if visited[n] == 0:
            #if not visited[n]:
            #if n not in visited:
                q.append(n) # 처리 큐
                ans_bfs.append(n)
                visited[n] = 1
 
def main(n:int, adj) -> int:

    # 오름차순 정렬
    for tmp in range(1, n+1):
        adj[tmp].sort()
        
    global ans_bfs, visited
    
    ans_bfs = []
    visited = [0]*(n+1)
    bfs(adj)

    return len(ans_bfs[1:])


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e = map(int, input().strip().split())
        adj[s].append(e)
        adj[e].append(s)
    
    ret = main(n, adj)
    print(ret)