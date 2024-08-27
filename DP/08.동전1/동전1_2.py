import sys

input = sys.stdin.readline
n, k = map(int, input().strip().split())
coins = [int(input().strip()) for _ in range(n)]

def main():
    dp = [0]*(k+1)  # 0원을 만드는 경우는 1가지 (아무 동전도 사용하지 않는 경우)
    dp[0] = 1   #dp[i][j]: i 번째 동전 추가시, j원을 만드는 경우의 수

    for i in coins:
        for j in range(i, k+1):
            dp[j] += dp[j-i] 
    
    return dp[k]

ret = main()
print(ret)