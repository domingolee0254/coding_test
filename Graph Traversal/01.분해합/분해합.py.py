################################################
# sol_1
################################################

# import sys

# input = sys.stdin.readline
# n = int(input().strip())

# for i in range(1, n+1):
#     x = i
#     rem = i
#     while x > 0:  # 0되면 종료
#         rem += x % 10 # 나머지
#         x = x // 10  # 나눠지는 수
#     if rem == n:
#         break
# else:
#     print(0)
#     exit(0)
# print(i)

################################################
# sol_2
################################################

import sys

input = sys.stdin.readline
n = int(input().strip())

tmp = []
for i in range(1, n+1): # 한자리 수 경우떄문에 인덱스 잘 처리하기, n이 아니라 n+1
    nums_str_list = list(str(i)) #['1', '0', '3']
    nums_int_list = list(map(int, nums_str_list)) #[2, 1, 5]
    sums = sum(nums_int_list)
    res = i + sums
    
    if res == n:
        print(i)  
        break
    if i == n: # 분해 안되는 경우, 한자리 수 
        print(0)