# 1. 시작점을 정하는 게 중요
# 2. 시작점을 정하고, 그 시작점에서 갈 수 있는 방향을 탐색
# 3. 종료조건
# 가장 작은 배열부터 채워나가기
# 작은 배열 채우는 패턴 -> 더 큰 배열 그리는 패턴 반복
# N -> 상하좌우 = N, N-1, N-1, N-2
import sys
input = sys.stdin.readline

# 입력
# n - 배열 만들기용 변수
# m - 위치 찾기용 변수
n = int(input())
m = int(input())
arr = [[0]*n for _ in range(n)]

# 1. 시작점 정하기(항상 정중앙)
x = (n-1) // 2
y = (n-1) // 2
arr[x][y] = 1 # 시작점의 value는 1

# 2. 시작점에서 갈 수 있는 방향 탐색
dx = [-1, 1, 0, 0] # 상, 하, 좌, 우의 x좌표(row이동)
dy = [0, 0, -1, 1]  # 상, 하, 좌, 우의 y좌표(col이동) 

i = 2 # 시작점 다음 숫자부터 진행
start_point = 3 # 3x3 배열부터 시작, 최소 배열의 크기

while x != 0 or y != 0: # 종료조건(x or y가 0이면 종료) - 배열의 최좌상단에 도달하면 종료
    while i <= start_point**2: # 채워나갈 숫자
        num_up, num_down, num_left, num_right = start_point, start_point-1, start_point-1, start_point-2 # 상, 하, 좌, 우의 이동 횟수(이동 패턴 반복)
        # 상 방향 이동
        if x == y == (n-1) // 2: # 일단 시작점에서 카운팅 하나 함
            x += dx[0]
            y += dy[0]
            num_up -= 1
        
        # 하 방향 이동
        elif num_down > 0: # 다 없어질 때 까지 이동해야하니까 0보다 클 때까지
            x += dx[0]
            y += dy[0]
            num_down -= 1
            
        # 좌 방향 이동
        elif num_left > 0:
            x += dx[0]
            y += dy[0]
            num_left -= 1
            
        # 우 방향 이동
        elif num_right > 0:
            x += dx[0]
            y += dy[0]
            num_right -= 1
        
        arr[x][y] = i
        i += 1

     # 작은 배열 하나 끝나면 -> 그리는 배열의 크기가 커짐-> 시작점을 다시 정해야함, start_point 바꿔줘야함  
    # 이해안됨
    n -= 2
       
# 시작점을 구하는 과정이 어려운데?
#  - start의 정확히 뭐지?