import sys
from collections import deque

def main() -> int:
    # 큐에 각 문서의 인덱스와 중요도를 튜플로 저장
    queue = deque([(i, p) for i, p in enumerate(D)])
    prt_idx = 0

    while queue:
        cur_idx, cur_priority = queue.popleft()

        # 현재 문서보다 중요도가 높은 문서가 있는지 확인
        if any(cur_priority < other_priority for _, other_priority in queue):
            queue.append((cur_idx, cur_priority))  # 중요도가 높은 문서가 있으면 큐의 맨 뒤로 보냄
        
        # 현재 문서의 중요도가 가장 높은 경우
        else:
            prt_idx += 1  # 현재 문서 인쇄후 인덱스 추가
            if cur_idx == M:  # 목표 문서가 인쇄되면 그 순서를 반환
                return prt_idx

input = sys.stdin.readline
T = int(input().strip())

ret_list = []
for _ in range(T):
    N, M = map(int, input().strip().split())
    D = list(map(int, input().strip().split()))
    
    res = main()
    ret_list.append(res)

for ret in ret_list:
    print(ret)
