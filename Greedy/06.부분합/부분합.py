##########################################################################
# sol 1 실패
##########################################################################

# def main(num_list:list) -> int:

#     start_idx = 0
#     end_idx = 0
#     min_sum = 0 
    
#     # 끝까지 갔을 때 종료(맨 마지막 값이 15일 수도 있으니까)
#     while start_idx <= len(num_list) - 1:
#         if sum(num_list[start_idx : end_idx+1]) < S:
#             end_idx += 1
            
#         elif sum(num_list[start_idx : end_idx+1]) >= S: 
#             min_sum = sum(num_list[start_idx : end_idx+1])
#             start_idx += 1
            
#         else:
#             pass
        
#     return min_sum

##########################################################################
# sol 2
##########################################################################
import sys

def main(S:int, num_list:list) -> int:
    # curr_sum: S와 비교하기 위함
    # min_len: 1. 최소 S를 찾았을 때 리턴할 그 부분의 길이를 구하기 위함
    #          2. inf 초기화 이유: 처음 비교되는 어떤 길이도 inf보다는 작을 것, min()부분에서 처음으로 조건에 맞을 때도 자동으로 갱신되게 하려고
    
    start_idx, end_idx = 0, 0
    curr_sum = 0 
    min_len = float('inf')
    
    # 마지막 인덱스가 리스트 끝까지 갈 때까지 돌림
    while end_idx < len(num_list):
        # end_idx 포인터를 이동시키면서 curr_sum을 증가
        while end_idx < len(num_list) and curr_sum < S:
            curr_sum += num_list[end_idx]
            end_idx += 1
        # 새로운 S를 찾았을 떄, 이전의 S와 비교후 어떤 게 최소인지 비교
        while curr_sum >= S:
            min_len = min(min_len, end_idx - start_idx)
            curr_sum -= num_list[start_idx]
            start_idx += 1
            
    # 최소 길이가 갱신되지 않았다면 0을 반환
    if min_len == float('inf'):
        return 0
    
    return min_len

if __name__=="__main__":
    input = sys.stdin.readline
    N, S = map(int, input().strip().split())
    num_list = list(map(int, input().strip().split()))
    ret = main(S, num_list)
    print(ret)
