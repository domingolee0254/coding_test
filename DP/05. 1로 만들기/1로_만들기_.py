# point: 이전 것에서 몇 

import sys

def main(N:int)->int: 
    
    dp = [0]*(N+1)
    
    for i in range(2, N+1): # 1은 연산 불가하므로 0으로 pass

        if i % 2 == 0 and i % 3 != 0: # 2배수일때만
            dp[i] = min(dp[i-1]+1, dp[i//2]+1)

        elif i % 3 == 0 and i % 2 != 0: # 3배수일때만
            dp[i] = min(dp[i-1]+1, dp[i//3]+1)

        elif i % 3 == 0 and i % 2 == 0: # 공배수일때는 어떤 걸해도 같음, 그 중에서도 최소인걸로 하기
            dp[i] = min(dp[i//2]+1, dp[i//3]+1)
    
        elif i % 2 != 0 and i % 3 != 0: # 5일 때
            dp[i] = dp[i-1]+1  

    return int(dp[N])

if __name__== "__main__" :
    input = sys.stdin.readline
    N = int(input().strip())
    ret = main(N)
    print(ret)
