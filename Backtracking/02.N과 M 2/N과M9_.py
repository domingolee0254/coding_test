import sys

def backtracking(n:int, cur_num_chains:list) -> list:
    global ans, used_num_one_hot, sorted_given_list # 글로벌로 선언해야 현재함수인 로컬함수에서 수정가능해짐
    if n == M: #M은 __main__ 스페이스에서 선언해서 글로벌로 됨, n
        ans.append(cur_num_chains)
        return
    
    prev = 0
    for j in range(N): # used_num_one_hot: visited 리스트
        # j는 숫자의 인덱스(9의 인덱스는 3,4) / n은 깊이(=수열의 길이)
        if used_num_one_hot[j] == 0 and prev != sorted_given_list[j]: # sorted_given_list의 j번째 숫자를 사용안한 경우 && 현재 값이 이전 값과 다른 경우(어차피 정렬되어서 이전 이후만 보면됨)
            used_num_one_hot[j] = 1 # 사용하고
            prev = sorted_given_list[j]
            backtracking(n+1, cur_num_chains+[sorted_given_list[j]]) # 수열 만들기, n+1이 종료조건될 타겟하는 수(M)라고 보면될듯, 그러면 그때까지의 수열을 리턴
            used_num_one_hot[j] = 0 # 사용 해제
        
    
def main(N:int, M:int, given_list:list) -> list:
    global ans, used_num_one_hot, sorted_given_list # 글로벌로 선언해야 bt함수에서 사용가능함
    sorted_given_list = sorted(given_list)
    ans = [] # 최종 리턴할, 가능한 모든 경우의 수 담음
    used_num_one_hot = [0]*N # 0-th idx는 버릴려고 [0]*N+1, n == m이어로 했는데 풀이보니까 N도 되던데? 
    # 중요한 것은 visited의 인덱스임 그게 0이나 1이나 어차피 리턴되는 것은 cur_num_chains의 값들이라 상관없는거지)
    # 근데 인덱스가 바뀌면 M도 M+1이나-1로 바뀌어야하는 거아닌가

    backtracking(0, []) # 초기값은 0으로 하고 0_th는 버릴 것
      
    return ans

if __name__=="__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    given_list = list(map(int, input().strip().split()))
    rets = main(N, M, given_list)
    for ret in rets:
        print(*ret)
        
        
# 
# 어려운 점1: 처음 9랑 나중 9랑 중복 처리할 때 visited의 인덱스 사용이 겹침
# 어려운 점2: 중복을 처리할 때 사용하는 visited 리스트의 목적과 인덱스 밸류의 기능을 명확히 알아야함
#            인덱스의 해당하는 번호가 사용되었다(중복되었다)는 것을 표시하는 것임
# 어려운 점3: 수열 반복 제거가 안됨
# 1 7
# 1 9
# 1 9

# used_num_one_hot is [0, 0, 1, 0]
# sorted_given_list is [2, 4, 4]

# used_num_one_hot is [0, 1, 0, 0]
# sorted_given_list is [2, 4, 4]
