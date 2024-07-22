import sys


def main(N:int) -> int:
    # 매우 큰 값으로 초기화
    INF = float('inf')
    
    # dp 배열을 매우 큰 값으로 초기화
    dp = [INF] * (N + 1)
    dp[0] = 0  # 0 kg은 봉지 0개로 가능
    
    # dp 배열 채우기
    for i in range(1, N + 1):
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + 1) # dp[i]가 INF로 초기화되어 가능함
        if i >= 5:
            dp[i] = min(dp[i], dp[i - 5] + 1)
    
    # dp[N]이 초기화된 값 그대로이면 정확한 무게를 만들 수 없음
    return dp[N] if dp[N] != INF else -1

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    
    ret = main(N)
    print(ret)