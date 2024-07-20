import sys

def main(coins:list, k:int) -> int:

    dp = [0]*(k+1)
    
    dp[0] = 1 # 만들 수 없는 경우 = 1
    
    # i = 각 동전의 종류
    # j = 만들 액수
    # dp[i][j] == 특정 i-th 동전으로 j-th액수를 만들 수 있는 경우의 수
    
    for i in coins:
        for j in range(i, k+1):
            dp[j] = dp[j] + dp[j-i] 
            # dp[j]는 이 행에서 저장된(이전 동전의 종류로 만들수 있는 경우의 수) 
            # + dp[j-i]는 거기에 새롭게 추가된 동전의 종류로만 만들수 있는 경우의 수
            # 그래서 i는 필요없음, 이미 dp[j]에 이전의 경우의 수가 다 들어있기 때문
                   
    return int(dp[j])

if __name__=="__main__":
    input = sys.stdin.readline
    n, k = map(int, input().strip().split())

    coins = [int(input().strip()) for _ in range(n)]
    
    ret = main(coins, k)
    print(ret)


