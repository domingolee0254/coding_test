
import sys

def main(N:int, k:int, coin_types:list)->int: 
    
    dp = [-1]*(k+1)
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3 
    dp[4] = 4 
      
    for i in range(5, k+1): # 1은 연산 불가하므로 0으로 pass

        if i % 12 == 0 and i % 5 != 0: # 12배수일때만
            dp[i] = i // 12

        elif i % 12 > 0 and (i % 12) % 5 == 0: # 12배수 + 5배수일때만
            dp[i] = (i // 12) + ((i % 12) // 5)

        elif i % 12 > 0 and (i % 12) % 5 > 0: # 12배수 + 5배수+ 나머지들은 1로 처리
            dp[i] = (i // 12) + ((i % 12) % 5)
    
    print(dp)
    return int(dp[N])

if __name__== "__main__" :
    input = sys.stdin.readline
    N, k = map(int, input().strip().split())
    coin_types = [int(input().strip()) for _ in range(N)]
    ret = main(N, k, coin_types)
    print(ret)
