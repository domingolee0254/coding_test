def solution(friends, gifts):
    answer = 0
    
    gift_tb_1 = [[0]*len(friends) for _ in range(len(friends))]
    gift_tb_2 = [[0]*3 for _ in range(len(friends))]
    
    for tmp1 in gifts: 
        fr, to = tmp1.split(' ') # fr, to = str
        gift_tb_1[friends.index(fr)][friends.index(to)] += 1

    
    tmp_col_list = [0]*len(friends)
    for i in range(len(friends)): # 0-3
        # row
        gift_tb_2[i][0] = sum(gift_tb_1[i])
        # col
        for j in range(len(friends)):
            tmp_col_list[j] += gift_tb_1[i][j]
    
    for k in range(len(friends)):
        gift_tb_2[k][1] = tmp_col_list[k] # 받은 선물
        gift_tb_2[k][2] = gift_tb_2[k][0] - gift_tb_2[k][1] # 지수

    
    bonus_gift = [0]*len(friends)
    for ii in range(len(friends)):
        for jj in range(len(friends)):
            
            # 조건 1: 선물을 주고 받았으나, 한 쪽이 더 큰 경우
            if gift_tb_1[ii][jj] > gift_tb_1[jj][ii]:
                bonus_gift[ii] += 1
                
            # 조건 2: 선물을 주고 받았거나, 안 받은 경우
            if gift_tb_1[ii][jj] == gift_tb_1[jj][ii]:  
                
                # 2-1. 자기 자신인 경우
                if ii == jj:
                    pass
                
                # 선물을 주고 받은데 같거나, 주고 받지 않은 경우(0-0, 2-2)
                elif ii != jj and gift_tb_1[ii][jj] == gift_tb_1[jj][ii]:
                    # 2-2. 타인끼리 주고 받지 않은 경우(0-0)
                    if gift_tb_1[ii][jj] == gift_tb_1[jj][ii] == 0:
                        # 지수비교
                        if gift_tb_2[ii][2] > gift_tb_2[jj][2]: # 지수 큰 쪽 +1
                            bonus_gift[ii] += 1  
                    
                    # 2-2. 타인끼리 주고 받았는데 같은 수 일 경우(2-2)
                    elif gift_tb_1[ii][jj] == gift_tb_1[jj][ii] != 0:
                        # 지수비교
                        if gift_tb_2[ii][2] > gift_tb_2[jj][2]: # 지수 큰 쪽 +1
                            bonus_gift[ii] += 1
                        elif gift_tb_2[ii][2] == gift_tb_2[jj][2]: # 지수 마저 같다면 pass
                            pass

    answer = max(bonus_gift)    
    return answer