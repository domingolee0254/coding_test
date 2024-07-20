import sys

def main(N:int) -> str:
    dp = [-1]*5001 # 0~5000까지의 인덱스를 가지는 dp 테이블, 0 th index는 사용하지 않음
    dp[3] = 1
    dp[5] = 1

    for i in range(6, N+1):
        if i % 3 == 0 and i % 5 != 0:
            dp[i] = dp[i-3] + 1
            # 오답 dp[i] = i // 3 # 3으로 나눈 횟수 == 옮긴 횟수
        elif i % 3 != 0 and i % 5 == 0:
            dp[i] = dp[i-5] + 1
        elif dp[i-3] > 0 and dp[i-5] > 0: # i-3, i-5 kg을 만드는 방법이 둘다 존재할 때(-1이 아니고 뭔가 값이 있을 때)
            dp[i] = min(dp[i-3]+1, dp[i-5]+1) # 그럴 떄는 둘 중 최소 이동횟수를 선택
        else:
            pass
        
    return int(dp[N])

if __name__=="__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    ret = main(N)
    print(ret)


