import sys
input = sys.stdin.readline

N, D = map(int, input().strip().split())
short_cuts = []

# 지름길이 실제로 거리를 줄일 수 있는 경우에만 리스트에 추가
for _ in range(N):
    start, end, length = map(int, input().strip().split())
    if end - start > length:
        short_cuts.append((start, end, length))
short_cuts.sort()

def main(N: int, D: int, short_cuts: list) -> int:
    # DP 배열 초기화: 각 위치까지의 최단 거리를 기본적으로 해당 위치까지의 거리로 설정
    dp = list(range(D + 1))  # dp[i]: i까지의 거리

    # 지름길 정보를 사용해 DP 배열을 업데이트
    for start, end, length in short_cuts:
        # 모든 지점을 순회하며 거리 갱신
        for i in range(1, D + 1):
            if end == i:
                # 현재 지점(end)이 지름길의 도착지점일 경우
                dp[i] = min(dp[i], dp[start] + length)
            else:
                # 그렇지 않은 경우, 이전 지점까지의 거리 + 1과 비교
                dp[i] = min(dp[i], dp[i - 1] + 1)

    return dp[D]

ret = main(N, D, short_cuts)
print(ret)
