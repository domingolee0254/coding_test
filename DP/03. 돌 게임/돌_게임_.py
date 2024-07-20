# 문제의 '완벽하게'? 가 무슨의미?: 그냥 딱 100에 맞게 끝내라는 뜻인듯, 2개 남았을 때 3개 가져가는 게 아니라, 합리적인 사람이라는 가정하에 진행하는 게임이라는 뜻인듯(지는 수를 두지 않고)
# optimal substructure: 전체 문제의 최적해가 부분문제의 최적해로부터 구해질 수 있는 성질
# overlapping subproblem: 부분문제들이 중복되는 성질
# 2^10 = 1024
# 언제 재귀를 쓰고 언제 DP를 쓰는가: 재귀는 코드가 간결하고 이해하기 쉽지만, 중복되는 계산이 많아서 시간복잡도가 높다. DP는 중복되는 계산을 저장해놓아서 시간복잡도를 줄일 수 있다.

# 어려운 부분1) dp[i] = not(dp[i-1] and dp[i-3])

import sys

# sk가 이기는 지를 기준(true) , 돌개수 볼 필요없음
def main(N):
    dp = [False]*(N+1)      # 이전의 결과들을 저장할 배열

    if N>=1:
        dp[1] = True
    if N>=3:
        dp[3] = True # 2인 경우는 False(cy가 이김)가 되니까 걍 그대로 둠

    for i in range(4, N+1):
        dp[i] = not(dp[i-1] and dp[i-3])
        # or 가 아닌 이유: 둘중 1개라도 False이면 됨(i-1이나 i-3 턴 사람이 지는 경우 == i 사람이 이기는 경우)
        # and로 묶여아함(f and f = f, f and t = f, f or f = f, f or t=t) 마지막 경우 때문에 or 안됨
        # dp[i] = not(dp[i-1] or dp[i-3])

    if dp[N] == True:
        return "SK"
    else:
        return "CY"

if __name__=='__main__':
    
    input = sys.stdin.readline
    N = int(input().strip())
    ret = main(N)
    print(ret)