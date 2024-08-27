import sys

input = sys.stdin.readline
N = int(input().strip())
board = [list(input().strip()) for _ in range(N)]

def main():
    # 8방향을 나타내는 델타 리스트
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]

    max_mines = 0  # 최대 지뢰 수를 세기 위한 변수 초기화

    # 모든 닫힌 칸('#')을 탐색
    for i in range(N):
        for j in range(N):
            if board[i][j] == '#':  # 만약 칸이 닫힌 칸('#')이면
                can_be_mine = True  # 이 칸이 지뢰가 될 수 있는지 가정

                # 이 닫힌 칸 주변의 8방향을 모두 확인
                for k in range(8):
                    ni, nj = i + dy[k], j + dx[k]  # 현재 칸(i, j)에서 k번째 방향으로 이동한 좌표(ni, nj)
                    
                    # 새로운 좌표가 보드 범위 내에 있는지 확인
                    if 0 <= ni < N and 0 <= nj < N:
                        if board[ni][nj].isdigit():  # 만약 주변 칸이 숫자 칸이면
                            num = int(board[ni][nj])  # 그 숫자 값을 가져옴
                            surrounding_mines = 0  # 그 숫자 칸 주변에 실제 지뢰가 몇 개 있는지 세는 변수
                            
                            # 그 숫자 칸(ni, nj)의 8방향을 다시 확인하여 실제 지뢰의 개수 계산
                            for l in range(8):
                                nni, nnj = ni + dy[l], nj + dx[l]  # 숫자 칸 주변 8방향 탐색

                                # 새로운 좌표(nni, nnj)가 보드 범위 내에 있는지 확인
                                if 0 <= nni < N and 0 <= nnj < N:
                                    if board[nni][nnj] == '*':  # 만약 지뢰가 있다면
                                        surrounding_mines += 1  # 주변 지뢰 수를 증가시킴

                            # 주변 지뢰 수(surrounding_mines)가 숫자 칸(num)이 가리키는 지뢰 수와 같거나 많으면
                            # 더 이상 지뢰를 놓을 수 없으므로 이 칸은 지뢰가 될 수 없음
                            if surrounding_mines >= num:
                                can_be_mine = False  # 이 닫힌 칸은 지뢰가 될 수 없음을 표시
                                break  # 더 이상 이 칸을 확인할 필요가 없으므로 중단
                
                # 현재 닫힌 칸이 지뢰가 될 수 있다면
                if can_be_mine:
                    max_mines += 1  # 지뢰가 될 수 있는 칸의 수를 증가시킴
                    board[i][j] = '*'  # 이 칸에 지뢰를 임시로 표시

    return max_mines

result = main()
print(result)