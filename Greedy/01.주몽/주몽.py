# 아이디어: 1. 연속되는 수가 아니라서 양쪽에서 포인터 이동
# 아이디어: 2. 좌우 - 우좌로 2번 계산되어서 2로 나눠줌
# 문제: 맞긴하나 시간이 오래걸림, 좌우방향에서 한번 계산되면 그 경우는 또 고려 안하는 거 해봐야겠음 
# 조합으로 풀어도 될거같음  

##########################################################################################
# sol 1) Two pointer approach # 32140KB	7516 ms	460B
##########################################################################################
import sys

def main(M:int, materials_list:list) -> int: 
    
    cnt = 0
    for left in materials_list:
        for right in reversed(materials_list):
            if left+right == M:
                cnt += 1
    return cnt // 2 # for 문이 좌우와 우좌가 2번 계산되어서 2로 나눠줌 
    # Left is 2
    # right is 7
    # Left is 7
    # right is 2
##########################################################################################
# sol 2) combination approach => 시간초과
##########################################################################################
# import sys
# from itertools import combinations

# def main(M, materials_list):
#     cnt = 0
#     for combi in combinations(materials_list, 2):
#         if sum(combi) == M:
#             cnt += 1
#     return cnt
    
if __name__=="__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    M = int(input().strip())
    materials_list = list(map(int, input().strip().split()))
    ret = main(M, materials_list)
    print(ret)