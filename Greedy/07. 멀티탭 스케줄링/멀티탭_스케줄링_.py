##############################################################################
# sol 1) 실패 
##############################################################################
# 빈도수 많은 순 정렬 후
# 콘센트 구멍 개수 넘치는 애들 개수 카운트

# import sys
# from collections import Counter

# def main(N, K, elec_list:str) -> str:
    
#     counter_dict = Counter(elec_list)
#     sorted_items = sorted(counter_dict.items(), key=lambda item: item[1], reverse=True)
#     return len(sorted_items[N:])

##############################################################################
# sol 2)
##############################################################################
import sys

if __name__=="__main__":
    input = sys.stdin.readline
    N, K = map(int, input().strip().split())
    elec_list = list(map(int, input().strip().split()))
    ret = main(N, K, elec_list)
    print(ret)
