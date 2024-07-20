################################################################################
# sol 1) backtracking 방식
################################################################################
# 가능한 모든 경우 실행 => 정답
# 중복체크 
# 종료 조건 
# 하부 함수 호출
import sys

def backtracking(n, proc_list):
    global ans, visited
    if n == M: # n: n번째 깊이, n번째 루프
        ans.append(proc_list)
        return

    for j in range(1, N+1): # 만들 진짜 경로, 수열이므로 j는 1부터 그 해당하는 숫자 N까지 가야함
        if visited[j] == 0:
            visited[j] = 1
            backtracking(n+1, proc_list+[j])
            visited[j] = 0 # 이 부분 어렵네, 왜 0으로 비워주지? 피피로 그림그려서 하면 이해될 듯

def main(N,M):
    global ans, visited
    ans = []
    visited = [0]*(N+1) # 왜 N으로 하면 인덱스 에러나지? visited의 목적이 뭐지? 이 벡터의 인덱스와 밸류가 의미하는 게 뭐지?
    # N+1로 해서 처음 0은 버리는 식으로 함
    # visited는 원핫벡터임(idx = 사용한 숫자, val = 1/0 사용했냐 안했냐, n번째 루프에서 찍어보면 현재까지 숫자 뭐뭐를 사용했나 알 수 있음)
    # n = depth를 의미
    # n depth visited의 idx등이 헷갈렸던게 뎁스와 숫자가 일치해서 헷갈렷음
    backtracking(0, [])
    # n은 0번째 부터 시작하는 것으로 함(호출함수 부분에서 방문 처리 해주려고)
    
    #     for i in range(1, N+1):
    #         # 자꾸 마지막에 [1],[2],[3],[4]가 들어감, 여기서 방문 처리를 안해줘서 그럼
    #         # so, 방문처리해주던지 dfs를 1번만 불러서(초기값은 0에서 시작), bt함수 내에서 1~n지 하는 방법있음 
    #         backtracking(i, [])
    return ans

if __name__=="__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    rets = main(N,M)
    for ret in rets:
        print(*ret)
        
################################################################################
# sol 2) permutations 방식 - 성공 
################################################################################
# import sys
# from itertools import permutations

# def main(N, M):

#     lst_total = [ _ for _ in range(1, N+1)]
#     lst = []
#     for ele in permutations(lst_total, M):
#         lst.append(ele)
#     return lst

# if __name__=="__main__":
#     input = sys.stdin.readline
#     N, M = map(int, input().strip().split())
#     rets = main(N, M)
#     for ret in rets:
#         for intg in ret:
#             print(intg, end=' ')
#         print()
