# 아이디어: (1) - (2) 일 때 2 부분이 커져야 함, -를 분기점으로 묶어서 한 파트는 더해서 한번에 빼주면 됨
# 뭉태기를 커지게 하고 그 뭉태기를 단위로 하나씩 빼는 거라서 그리디인가?

import sys

def main(num_str:str) -> int:
    num_with_plus_sign_combine_str_list = num_str.split('-') #['55', '50+40']
    curr_sum = sum(map(int, num_with_plus_sign_combine_str_list[0].split('+'))) 
    
    for tgt in num_with_plus_sign_combine_str_list[1:]: # tgt = ['55', '50+40'] 한 덩어리씩 순회
        curr_sum -= sum(map(int, tgt.split('+'))) #한 덩어리의 합을 통째로 빼주면 됨, 숫자+부호가 문자열이므로 +를 기준으로 뜯어서 int로 더한 다음에 한번에 빼주기

    return curr_sum

if __name__=="__main__":
    input = sys.stdin.readline
    num_str = input().strip()
    ret = main(num_str)
    print(ret)