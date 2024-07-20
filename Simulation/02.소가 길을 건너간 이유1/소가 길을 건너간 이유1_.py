# idea: 소의 위치를 저장하는 리스트 필요, 리스트의 각 인덱스는 그에 해당하는 th 번째 소
# [-1]*(n+1) 할 때 문제에서 말하는 인덱스랑 파이썬 인덱스랑 차이가 있으니 잘 보기

import sys
input = sys.stdin.readline
n = int(input())
mv_list = [-1]*(n+1) # 소의 이동 저장하는 리스트
cnt=0

for _ in range(n):

    # print(_)
    cow_idx, cow_move = map(int, input().split())

    if mv_list[cow_idx] == -1: # th 번째의 소의 위치가 처음으로 입력될 때
        mv_list[cow_idx] = cow_move
    else: # th 번째의 소의 위치가 입력되는 게 처음이 아닐 때
        if mv_list[cow_idx] != cow_move:# 위치 이동 변화 있을 때
            mv_list[cow_idx] = cow_move
            cnt += 1

print(cnt)