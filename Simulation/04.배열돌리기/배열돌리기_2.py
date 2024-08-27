import sys

# 행렬을 시계 방향으로 45도 회전하는 함수
def rotate_45_clockwise():
    mid = n // 2  # 행렬의 중앙 인덱스를 계산
    # 행렬에서 주요 요소를 추출
    main_diagonal = [matrix[i][i] for i in range(n)]  # 주 대각선
    center_column = [matrix[i][mid] for i in range(n)]  # 중앙 열
    anti_diagonal = [matrix[n-1-i][i] for i in range(n)]  # 부 대각선
    center_row = matrix[mid][:]  # 중앙 행

    # 새 위치에 요소를 배치
    for i in range(n):
        matrix[i][mid] = main_diagonal[i]  # 주 대각선 -> 중앙 열
        matrix[i][n-1-i] = center_column[i]  # 중앙 열 -> 부 대각선
        matrix[mid][i] = anti_diagonal[i]  # 부 대각선 -> 중앙 행
        matrix[i][i] = center_row[i]  # 중앙 행 -> 주 대각선

# 메인 함수
def main():
    if n == 1:
        return matrix  # 크기가 1x1인 경우, 변화 없이 반환

    steps = (d // 45) % 8  # 회전해야 할 스텝 수 계산
    if steps < 0:
        steps += 8  # 음수인 경우 양수로 조정

    for _ in range(steps):
        rotate_45_clockwise()  # 주어진 스텝 수만큼 45도 회전
    
    results.append(matrix)  # 결과를 결과 리스트에 추가
    
    return 0  # 함수 종료

input = sys.stdin.readline  # 입력을 받기 위한 함수 설정
t = int(input().strip())  # 테스트 케이스의 수 입력 받음
results = []  # 각 테스트 케이스의 결과를 저장할 리스트

for _ in range(t):
    n, d = map(int, input().split())  # 행렬 크기 n과 회전 각도 d 입력 받음
    matrix = [list(map(int, input().split())) for _ in range(n)]  # 행렬 데이터 입력 받음
    main()  # 메인 함수 실행

for result in results:
    for row in result:
        print(" ".join(map(str, row)))  # 결과 행렬을 출력
