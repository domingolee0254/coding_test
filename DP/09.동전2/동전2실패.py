###################################################################################
# sol 1) 틀림, 반례 3 11 1 5 6
###################################################################################
import sys
import copy

def main(n, k, coins):
    INF = int(1e9)
    tb = [[INF]*(k+1) for _ in range(n+1)]
    # 초기값

    # 아래 메인 돌 때 최소값 구할 때 0입력되어서 첫 열만 채워주려고 무한으로 초기화
    for tmp in tb:
         tmp[0] = 0
    k_tmp = copy.deepcopy(k)    

    # k가 배수가 아니라면 못 구함
    sorted_coins = sorted(coins)
    for div_idx in reversed(range(len(sorted_coins))):
        k_tmp = k_tmp % coins[div_idx]
    if k_tmp != 0: 
        return -1
    
    for i in range(1, n+1): # i = 0
        for j in range(1,k+1): # j = 1 ~ 15
                tb[i][j] = min(tb[i][j-coins[i-1]] + 1, tb[i-1][j])
    return tb[i][j]

if __name__=="__main__":
    input = sys.stdin.readline
    n, k = map(int, input().strip().split())
    coins = [int(input().strip()) for _ in range(n)]
    ret = main(n, k, coins)
    print(ret)

###################################################################################
# sol 2) 틀림, 반례 3 11 1 5 6
###################################################################################
# 큰 액수의 동전을 최대한 많이 사용
# 1개의 종류의 동전만 사용했을 때랑 / 여러 개 종류의 동전을 섞어썼을 때랑 개수 비교 
# => 사용 동전의 개수가 최소가 되도록

# 어려운 점1: 최종 8을 구하는 데, 3을 구할 때 동전 '2'만 있으면 안만들어지는 데 매트릭스에 0을 넣음?
# => 안만들어지면 위에 것을 그대로 받아옴 

# import sys
# import copy

# def main(n, k, coins):
#     tb = [[0]*(k+1) for _ in range(n+1)]
#     # 초기값
#     INF = int(1e9)
#     tb[:][0] = 0

#     # 아래 메인 돌 때 최소값 구할 때 0입력되어서 첫 열만 채워주려고 무한으로 초기화
#     for tmp in range(len(tb)):
#         if tmp == 0:
#             tb[tmp][:] = [INF]*(k+1)
#         else:
#             break
    
#     k_tmp = copy.deepcopy(k)    

#     # k가 배수가 아니라면 못 구함
#     sorted_coins = sorted(coins)
#     for div_idx in reversed(range(len(sorted_coins))):
#         k_tmp = k_tmp % coins[div_idx]
#     if k_tmp != 0: 
#         return -1
    
#     for i in range(1, n+1): # i = 0
#         for j in range(1,k+1): # j = 1 ~ 15
#             # j가 어떤 동전5의 배수라면 인덱스 5번째 이전 것에서 + 1(10은 동전 5 2개로 만들 수 있으니까)  
#             # if j % coins[i-1] == 0:
#                 #같은 행의 동전 1개 직전 개수 / 윗 행의 동전 개수 중 최소인 것 선택
#                 tb[i][j] = min(tb[i][j-coins[i-1]] + 1, tb[i-1][j])
#             # else:
#                 # 하나 추가되었을 때 만들수 있는 수(좌)과 이전까지 주어진 동전 종류로 만들수 있는 것(상)
#                 # tb[i][j] = min(tb[i][j-1] + 1, tb[i-1][j])
    
#     print(tb)
#     # tb[i][j] = 액수 i를 만드는 데 까지 j개의 동전이 있을 때 들어간 최소 동전 개수
#     # 총액 15를 만드는 데 3(1,5,12)로 만드는 데 들어간 최소 동전 개수
#     return tb[i][j]

# if __name__=="__main__":
#     input = sys.stdin.readline
#     n, k = map(int, input().strip().split())
#     coins = [int(input().strip()) for _ in range(n)]
#     ret = main(n, k, coins)
#     print(ret)
