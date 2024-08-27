import sys
from collections import deque

def main() -> list:
    queue = deque(range(1, N+1))
    result = []

    while queue:
        # K-1만큼 회전해서 K번째 사람이 앞에 오도록 함
        queue.rotate(-(K-1))
        # K번째 사람을 제거하고 결과 리스트에 추가
        result.append(queue.popleft())

    return result

input = sys.stdin.readline
N, K = map(int, input().strip().split())
ret = main()

print(f"<{', '.join(map(str, ret))}>")