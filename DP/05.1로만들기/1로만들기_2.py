import sys

def main(N:int) -> int:
    dp = [[0]*(N+1)]
    dp[1] = 0

    for i in range(2, N+1):
        # -1 연산을 미리해주고 2와 3으로 나눠떨어지면 1이 만들어진 꼴이므로 항상 먼저 해주고 뒤 if문 돌림
        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            # -1 미리한 최소값과 비교
            dp[i] = min(dp[i], dp[i // 2]+1)

        elif i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3]+1)
    
    return dp[N]

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input().strip())    
    ret = main(N)
    print(ret)