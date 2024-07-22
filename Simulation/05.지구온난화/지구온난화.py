import sys
import copy
    
def main(R:int, C:int, cur_map:list) -> list:
    # fifty_map = [["."]*C for _ in range(R)]
    # 이걸로하면 .때문에 새롭게 X로 업데이트된 부분 때문에 반복문의 다음 행에서 잘못계산됨, 그래서 빈 맵이 아니라 원래 맵 복사해서 사용하는 게 나음
    fifty_map = copy.deepcopy(cur_map)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    r_min = sys.maxsize
    r_max = -1   
    c_min = sys.maxsize
    c_max = -1
    # 예외 처리: 한개만 있을 경우
    if R == 1:
        if C == 1: 
            if cur_map[0][0] == 'X':
                return [['X']]
            elif cur_map[0][0] == '.':
                return [['.']]
        else:
            pass
        
    for i in range(R):
        for j in range(C):
            cnt = 0
            for dir_dix in range(4):
                nx = j + dx[dir_dix]  
                ny = i + dy[dir_dix]
                # 지도 벗어나지 않을 때
                if (0<=nx<C) and (0<=ny<R):
                    if cur_map[ny][nx] == ".":
                        cnt += 1
                # 지도 벗어날 때
                elif nx < 0 or nx >= C or ny < 0 or ny >= R:
                    cnt += 1    
                
            if cnt >= 3:
                fifty_map[i][j] = '.'
            else: 
                pass
 
    # 범위 재조정
    for r in range(R):
        for c in range(C):
            if fifty_map[r][c] == 'X':
                r_min = min(r, r_min)
                r_max = max(r, r_max)                
                c_min = min(c, c_min)
                c_max = max(c, c_max)
    
    # 한 개도 없을 경우
    if r_min == sys.maxsize or r_max == -1 or c_min == sys.maxsize or c_max == -1:
        return [['X']]
    
    # 계속 틀렸던 부분
    # result = [row[c_min:c_max + 1] for row in fifty_map[r_min:r_max + 1]]
    # return result    
    # 반복문을 돌릴 지 / 이차원 리스트는 인덱싱이 안되는 지 검토중
    # 단일 행일때의 처리가 계속 안되던거 같은데 왜 안되는 지 모르겠음
    # 반례
    # 4 4
    # ....
    # .XX.
    # .X..
    # ....

    tmp_ret = []
    if r_min == r_max and c_min == c_max:
        return [fifty_map[r_min][c_min]]
    
    elif r_min == r_max and c_min != c_max:
        for tmp_idx_1 in range(r_min):
            if tmp_idx_1 == r_min:
                return [fifty_map[r_min][c_min:c_max+1]]
    
    elif r_min != r_max and c_min == c_max:
        for tmp_idx_2 in range(r_min, r_max+1):
            tmp_ret.append([fifty_map[tmp_idx_2][c_min]])
        return tmp_ret

    # r_min != r_max and c_min != c_max:        
    elif r_min != r_max and c_min != c_max:
        for tmp_idx_3 in range(r_min, r_max+1):
            tmp_ret.append(fifty_map[tmp_idx_3][c_min:c_max+1])
        return tmp_ret
    
if __name__ == "__main__":
    input = sys.stdin.readline
    R, C = map(int, input().strip().split())
    cur_map = [list(input().strip()) for _ in range(R)]
    rets = main(R, C, cur_map)
        
    for ret in rets:
        print(''.join(ret))
        # print(*ret)으로 해서 계속 한칸 \s가 들어가서 틀림
