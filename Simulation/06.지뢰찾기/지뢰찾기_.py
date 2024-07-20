# 1. 문제 이해 
# 4. 아이디어
#   4.1. 입력은 배열로 받기
#   4.2. 지뢰 배열에서는 *개수 세기
#   4.3. X 배열에서는 마지막 X에 도달하기
#   - 뭔가 저장할 같은 사이즈의 배열도 필요해보임
#   4.4. (한행 접근-> 반복문) X 끝에서 멈추면 -> 8 방향 탐색 [-1, 1, 0, 0] [0, 0, -1, 1] / [-1, -1, 1, 1] [-1, 1, -1, 1]
#   4.5. 탐색중에 *이 있다 -> cnt +=1 -> 멈추고 -> 그자리(위치 좌표 필요) -> 해당 숫자 저장
#   4.6. 나머지 온점 채우기 , 0 처리
# game_over 함수 안만들었었음

##############################################################################################################################
# 1번쨰 시도
##############################################################################################################################

# import sys
# input = sys.stdin.readline

# n = map(int, input().split()) 
# gt_mat = [input().split() for _ in range(8)]
# game_mat= [input().split() for _ in range(8)]


# # 8방향 - 상,하,좌,우, 좌상, 우상, 좌하, 우하
# dx = [-1, 1, 0, 0, -1, -1, 1, 1]
# dy = [0, 0, -1, 1, -1, 1, -1, 1]



# # 1. 상 
# # 2. 하 
# # 3. 좌
# # 4. 우
# # 5. 좌상
# # 6. 우상
# # 7. 좌하
# # 8. 우하
# def find_mine(dx, dy, gt_mat): 
#     cnt = 0
#     for i in range(8):
#         if dx[i] == False or dx[i-1] == False:
#             pass
#         else:
#             if gt_mat[dx[i]][dy[i]] == '*':
#                 cnt += 1
#             else:
#                 pass
#     return cnt
    
# # 마지막 X를 위한 반복문
# # 게임 행렬에서 row하나씩 접근
# for game_row in game_mat:
#     # 접근한 row에서 col이동(마지막 X나올 때까지 str안에서 반복)
#     for tmp_row_idx, tmp_row_value in enumerate(game_row): # game_row = '...xxx' 리스트의 한 요소
#         for tmp_char_idx, tmp_char_val in enumerate(tmp_row_value): # tmp_row = ...xxx(str) / 각각의 캐릭터의 인덱스를 구함. 
#             if tmp_char_val == ".":
#                 if tmp_row_value[tmp_char_idx-1] == 'x': #upper 뭐 이런거 해야하나? 대문자 소문자 구분없이 처리하는 거 (입력부분에서?)
#                     # tmp_char_idx-1 = 마지막 x의 위치
                        
#                     # 여기에 기준 x에서 8방향에서 지뢰찾고 카운트하느 함수 필요
#                         num_mine = find_mine(dx, dy, gt_mat)
#                     # 여기서 그 x에서에서의 '좌표'와 'value'를 다시 저장하기
#                         print(num_mine)
#                 else: # .을 찾았는데 그 뒤 거도 .이면 패스
#                     pass
                
# ##############################################################################################################################

##############################################################################################################################
# 2번쨰 시도
##############################################################################################################################
# n = map(int, input().strip())으로 하니까 TypeError: 'map' object cannot be interpreted as an integer 에러남
# n = int(input().strip())이 맞음
# 1. 1차 시도때 하려다가 안되었던 ['xxx.....', 'xxx.....'] 이런식으로 하나의 스트링을 한 row 자체가 되었던 게(입력받을 때 잘못한 듯) 고쳐짐 -> ['.', '.', '.', '*', '*', '.', '.', '*']
# 2. find_mine()에서 가장자리에서 위로(배열이 넘쳐서) 못올라가서 index error났던거 극복 - 종료조건 잘 주면된다. 
import sys
input = sys.stdin.readline

n = int(input().strip())
# gt_mat = [input().strip() for _ in range(n)]
# game_mat= [input().strip() for _ in range(n)]
gt_mat = [] #지뢰 위치담을 배열
game_mat = [] #열린칸 위치담을 배열

for i in range(n): # 입력값 받기
    gt_row = list(map(str, input().strip()))
    gt_mat.append(gt_row)                                        # print(map(str, input().strip())) <map object at 0x0000021323637160>

for i in range(n):
    exec_row = list(map(str, input().strip()))
    game_mat.append(exec_row)

# 8방향 - 상,하,좌,우, 좌상, 우상, 좌하, 우하
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def find_mine(x, y): 
    cnt = 0 
    for i in range(8): #8방향
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n: # 종료되는 조건: 배열의 범위 초과될 때 continue로 건너뛰기
            continue
        # x,y은 0~7 nx<0 --- (-1이면 안됨, =가 없는 이유는 배열의 인덱스가 0일 때는 유효하기 때문), 
        # nx<=N(x는 7까지니까 8까지가면 안됨,  =가 포함된 이유는 nx가 N에 도달했을 때도 범위를 벗어난 것)
        if gt_mat[nx][ny] == "*":
            cnt += 1
    
    return cnt

def game_over(): # 지뢰 밟았을 떄 실행(지뢰 있는 모든 gt 다 공개)
    for i in range(n):
        for j in range(n):
            if gt_mat[i][j] == "*":
                game_mat[i][j] = "*"

# main
for i in range(n):
    for j in range(n):
        if game_mat[i][j] =='x': # 게임맵이 x로 열려있다면 그거 기준 8방향의 지뢰 개수 세야 함
            game_mat[i][j] = find_mine(i, j)
            if gt_mat[i][j] == "*": # 열었는데 지뢰가 있었다면
                game_over() # 게임오버 함수 실행

for k in game_mat:
    for l in k:
        print(l, end='')
    print()