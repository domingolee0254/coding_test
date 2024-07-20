####################################################
# sol_1
####################################################

# import sys
# input = sys.stdin.readline

# input_list = [int(input().strip()) for x in range(1,10)]

# excluded_lists = []
# for exclude_1 in input_list:
#     curr_list= []
#     for i in input_list:
#         if exclude_1!=i:
#             curr_list.append(i)
#     for exclude_2 in curr_list:
#         curr_list_2 = []
#         for j in curr_list:
#             if exclude_2 !=j:
#                 curr_list_2.append(j)
#             excluded_lists.append(curr_list_2)

# for k in excluded_lists:
#     tmp = sum(k)
#     if tmp == 100:
#         for l in sorted(k):
#             print(l)
#         break
    
####################################################
# sol_2
####################################################
import sys
import itertools

input = sys.stdin.readline

input_list = [int(input().strip()) for x in range(1,10)]
combination_list = list(itertools.combinations(input_list, 7)) # permu해도 되는 데 경우가 너무 많아짐

for k in combination_list:
    tmp = sum(k)
    if tmp == 100:
        for l in sorted(k):
            print(l)
        break
    