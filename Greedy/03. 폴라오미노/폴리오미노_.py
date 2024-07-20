# 1. 4개짜리 먼저 되는 지 확인 
# 2. 4개짜리 되는 지 확인
# 3. 안되는 애들 -1
# 문자열은 변경 불가능(immutable) 하기에 문자열에 직접 replace하는 방법보다 리스트에 append하는 게 좋음

import sys
from collections import Counter

def main(tgt_str:str) -> str:

    converted_list = []
    idx = 0
    while idx < len(tgt_str):
        if idx+3 < len(tgt_str) and tgt_str[idx:idx+4]=="XXXX":
            converted_list.append("AAAA")
            # converted_list[idx:idx+4].append("AAAA") 이런 문법 없음
            idx += 4
        elif idx+1 < len(tgt_str) and tgt_str[idx:idx+2]=="XX":
            converted_list.append("BB")
            idx += 2
        elif tgt_str[idx] == ".":
            converted_list.append(".")
            idx += 1
        else:
            return -1
    converted_str = ''.join(converted_list)
    return converted_str

if __name__=="__main__":
    input = sys.stdin.readline
    tgt_str = input().strip()
    ret = main(tgt_str)
    print(ret)
    
    
######################################################################
# 실패 솔루션 1 - 경우를 나누려니 너무 조잡해짐
###################################################################
# def main(X_str:list) -> str: 

#     X_list = [item for item in X_str.split('.') if item] # '' 부분 없애기 ''은 불리언에서 False로 나옴
#     for i in X_list:
#         c = Counter(i)
        
#         if c[1] == 1:
#             return -1

#         elif c[1] % 2 == 1:

#         elif c[1] == 2:

#         elif c[1] % 4 == 0 and c[1] != 2:    

#         elif c[1] % 2 == 0 and c[1] % 4 != 0 and c[1] != 2:    

    
######################################################################
# 실패 솔루션 2
#####################################################################
# 문자열은 변경 불가능(immutable) 하기에 문자열에 직접 replace하는 방법보다 리스트에 append하는 게 좋음
# def main(tgt_str:list) -> str:

#     idx = 0
#     while idx < len(tgt_str):
#         if idx+3 < len(tgt_str) and tgt_str[idx:idx+4]=="XXXX":
#             tgt_str[idx:idx+4] = tgt_str[idx:idx+4].replace("XXXX", "AAAA")
#             print(f"tgt_str is {tgt_str}")
#             idx += 4
#         elif idx+1 < len(tgt_str) and tgt_str[idx:idx+2]=="XX":
#             tgt_str[idx:idx+2] = tgt_str[idx:idx+2].replace("XX", "BB")
#             idx += 2
#         elif tgt_str[idx] == ".":
#             idx += 1
#         else:
#             return -1
        