# 1. 크게 더해지는 것을 없애야함, 큰 액수인 애들을 없애야 함 - 바구니안에서 마지막 +1 되는 애로 없애줘야 함
# 가장 마지막 바구니에서 1개로 남는 게 그 리스트에서 최소값이어야함.
# 그게 큰 값이더라도 -2번째로 큰 값이 더해지는 것보다 -1 번째로  큰 값이 더해지는 게 나음 
# 이러한 점에서 그리디로 풀어야할 듯
# => 소트 후 3개 씩 묶기
 
import sys


def main(dairy_cost:list) -> int:

    i = 0
    sorted_list = sorted(dairy_cost, reverse=True)
    aggre_list = []
    
    # 3개씩 묶을 건데 그 조건에 부합할 때
    while i + 2 < len(sorted_list):
        aggre_list.extend(sorted_list[i:i+2])
        i += 3
    
    #1,2개라서 애초에 조건에 안맞거나 위에서 하고 1~2개 남았을 때 더해주기
    if i+2 >= len(sorted_list):
        aggre_list.extend(sorted_list[i:])  # append는 리스트 자체를 넣고, extend는 원소만 넣음, 최종 정리된 리스트에서 sum 하려고 extend 사용 

    return sum(aggre_list)
    
if __name__=="__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    dairy_cost = [int(input().strip()) for _ in range(N)]
    ret = main(dairy_cost)
    print(ret)
