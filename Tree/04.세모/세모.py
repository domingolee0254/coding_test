import sys

def solve_minimal_distance_tree(N):
    # 거리의 합을 계산
    return (N-1)**2

if __name__=="__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    ret = solve_minimal_distance_tree(N)
        
    # 출력 1: 최소 거리의 합
    print(ret)
    
    # 출력 2: 간선 정보
    for i in range(2, N+1):
        print(1, i)