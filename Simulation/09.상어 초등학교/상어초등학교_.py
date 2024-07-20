import sys

def setting_seat(st_table:list, dx:list, dy:list) -> list:
    
     # 한 명씩 받으면서 선호 학생있는지 확인
    for st in st_info:
        cur_st_idx = st[0]
        cur_st_fav = st[1:]
        
        vacs = []
        for y in range(N):
            for x in range(N):
                if st_table[y][x] == 0:
                    fav_cnt = 0
                    vac_cnt = 0 
                    # 어디로 갈지
                    for dir_idx in range(4):
                        nx = x + dx[dir_idx]
                        ny = y + dy[dir_idx]
                        
                        # 범위 체크
                        if nx < 0 or ny < 0 or nx >= N or ny >= N:
                            continue                            
                        # 선호 학생이 있는 근처로 가는데, 비어있는지 확인 후 가장 많이 비어있는 곳 확인 후, 적은 행 , 적은 열로 가기

                        if st_table[ny][nx] in cur_st_fav:
                            fav_cnt += 1
                            
                        if st_table[ny][nx] == 0:
                            vac_cnt += 1
                            
                    vacs.append([fav_cnt, vac_cnt, y, x])
        vacs.sort(key=lambda x:(-x[0], -x[1], x[2], [3]))
        st_table[vacs[0][2]][vacs[0][3]] = cur_st_idx
    
    return st_table

def check_pleasure(st_info:list, comp_table:list) -> int:
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    st_info.sort()
    per_stu_pl = 0
    
    for cur_y in range(N):
        for cur_x in range(N):
            adj_fav_cnt = 0
            st_num = comp_table[cur_y][cur_x]

            for dir_idx_2 in range(4):
                nx = cur_x + dx[dir_idx_2]
                ny = cur_y + dy[dir_idx_2]
    
                # 범위 체크
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue                    
    
                if comp_table[ny][nx] in st_info[st_num - 1][1:]:
                    adj_fav_cnt += 1  
                    
            if adj_fav_cnt > 0:
                # 10의 지수로 계산
                per_stu_pl += (10 ** (adj_fav_cnt - 1))

    return per_stu_pl

def main(N:int, st_info:list) -> int:
    st_table = [[0]*N for _ in range(N)]
    
    # 초기값 설정
    dx = [-1, 1, 0, 0,]
    dy = [0, 0, -1, 1]
    
    comp_table = setting_seat(st_table, dx, dy)
    pleasure = check_pleasure(st_info, comp_table)

    return pleasure

if __name__=="__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    st_info = [list(map(int, input().strip().split())) for _ in range(N**2)]
    ret = main(N, st_info)
    print(ret)