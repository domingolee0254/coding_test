# 1. tgt = 라인 돌리기 부분, 움직일 list = 주대각, 부대각, 가운데 행, 가운데 열 => 4개
# 2. 복사할 matrix 하나 초기화
# 3. 안 바뀌는 부분(정가운데, 빈 곳), 빈곳은 원래 0으로 new_mat으로 해두고 0인 부분은 for 문 돌면서 그 부분만 0이면 원래 mat에서 인덱스로 접근해서 복사하기  
# 4. 음수 각도 = -(360 - 양수 각도)
# 5. 회전 규칙 경우의 수 다 나누기
# 6. 초기 점(대각선으로 하면 0,0 지점이 회전 시에 어디로 가는 지) 지정

# 5. 회전 규칙 경우의 수 다 나누기 -> 잘못접근함. 그냥 인덱싱을 각 4개의 경우로 나누고 -> 예를 들면 한 대각선이 갈수 있는 8가지로 접근하는 게 맞음.
# 


########################################################################
# 1번째 방식 -> 실패
########################################################################

# import sys
# input = sys.stdin.readline

# T = int(input().strip())

# main_diag = []
# sub_diag = []
# row = []
# col = []

# for i in range(T):
#     n, d = map(int, input().split())    
#     og_mat = [list(map(int, input().split())) for _ in range(n)]
#     turned_mat = [[0]*n for _ in range(n)]
    

# # 45 d
# for i in range(n):
#     for j in range(n):
#         main_diag.append(og_mat[i][j])
        
        
# for i in range(n):
#     turned_mat[i][n+1//2] = main_diag[i]
    
########################################################################
# 2번째 방식
########################################################################

def rotate_matrix(n, d, matrix):
    rotations = d // 45 % 8  # 회전 횟수 => 360도는 45도를 1회전으로 하면 8회전이므로 모듈러로 계산(정수론의 나머지 정리)
    for _ in range(rotations):
        # 임시 변수로 주 대각선, 중앙 열, 부 대각선, 중앙 행의 원소를 저장
        main_diag = [matrix[i][i] for i in range(n)]
        mid_col = [matrix[i][(n+1)//2-1] for i in range(n)]
        sub_diag = [matrix[i][n-i-1] for i in range(n)]
        mid_row = matrix[(n+1)//2-1][:]

        # 시계 방향으로 원소 이동
        for i in range(n):
            matrix[i][(n+1)//2-1] = main_diag[i]  # 주 대각선 -> 중앙 열
            matrix[i][n-i-1] = mid_col[i]  # 중앙 열 -> 부 대각선
            matrix[(n+1)//2-1][n-i-1] = sub_diag[i]  # 부 대각선 -> 중앙 행
            matrix[i][i] = mid_row[i]  # 중앙 행 -> 주 대각선

    return matrix

# 입력 받기
T = int(input().strip())  # 테스트 케이스의 수

for _ in range(T):
    n, d = map(int, input().split())  # 배열의 크기 n과 회전 각도 d
    matrix = [list(map(int, input().split())) for _ in range(n)]  # 초기 매트릭스

    # 회전 실행
    rotated_matrix = rotate_matrix(n, d, matrix)

    # 회전된 매트릭스 출력
    for row in rotated_matrix:
        print(*row)


for tmp_list in range(len(final_mat)):
    print(*tmp_list)
