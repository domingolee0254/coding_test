#######################################################################################
# sol 1) just 구현 187256 KB	1932 ms
#######################################################################################
# 아이디어: 1. 파이썬 sort = 팀 소트 = nlogn
# 아이디어: 2. 중복되는 요소 제거하라는 말 없어서 그냥 concat으로 처리, 중복되는 거 1개로 처리할거였으면 set을 사용하는 게 좋을듯
# 문제: 맞았으나 시간이 너무 오래걸림, 메모리도 너무 큰거같음(큰건가?-확인필요)

# import sys

# def main(N:int, M:int, list_A:list, list_B:list) -> list: 
    
#     list_concat = list_A + list_B
#     sorted_list = sorted(list_concat)
    
#     return sorted_list

#######################################################################################
# sol 2) 투 포인터 => 실패
#######################################################################################
# import sys

# def main(N:int, M:int, list_A:list, list_B:list) -> list: 
    
#     list_concat = list_A + list_B
#     # 문제: 주어진 배열에서 정리하는 게 아니라 새로운 저장 공간을 만들어서 넣어야함.
#     for i in range(1, len(list_concat)+1):
#         if list_concat[i-1] > list_concat[i]:
#             list_concat[i-1], list_concat[i] = list_concat[i], list_concat[i-1]
        
#     return list_concat

#######################################################################################
# sol 3) 투 포인터 305548KB 1444ms 
#######################################################################################
# 아이디어: 1. 두 배열을 동시에 순회하면서 더 작은 값을 결과에 추가
# 아이디어: 2. 두 배열의 길이가 다를 때 -> 2.1 한 배열을 모두 순회한 후 남은 원소들을 결과에 추가, 
#                                       2.2 이동한 포인터는 이전 루프에서의 인덱스를 저장 so, 그것을 이용하면 됨
# 문제: 왜 투 포인터가 메모리가 더 크지?
import sys

def main(N:int, M:int, list_A:list, list_B:list) -> list:

    result = []  # 결과 저장할 리스트
    left = right = 0  # 두 배열의 포인터 초기화

    # 두 배열을 동시에 순회하면서 더 작은 값을 결과에 추가
    while left < N and right < M: # 두 조건이 모두 참일 때만 실행(인덱스가 적용될 때까지만), 두 배열 중 하나라도 끝에 도달하면 종료
        if list_A[left] < list_B[right]:
            result.append(list_A[left])
            left += 1
        else:
            result.append(list_B[right])
            right += 1

    # print(f"result first loop: {result}\n\n") # result first: [1, 2, 3, 4, 5, 7]
      
    # 한 배열을 모두 순회한 후 남은 원소들을 결과에 추가
    # 두 배열 중 하나 끝나면 남은 배열의 원소들을 결과에 추가
    while left < N:
        result.append(list_A[left])
        left += 1 # left라는 인덱스는 위에서 사용하면서 현재까지의 인덱스를 저장하고 있음
        # print(f"result left < N: {result}\n\n") # result left  < N: [1, 2, 3, 4, 5, 7, 9]

    while right < M:
        result.append(list_B[right])
        right += 1
        # print(f"result right < M: {result}\n\n")

    return result

if __name__=="__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    list_A = list(map(int, input().strip().split()))
    list_B = list(map(int, input().strip().split()))
    ret = main(N, M, list_A, list_B)
    
    print(" ".join(map(str, ret)))

    # for i in ret:
    #     print(i, end=" ")
