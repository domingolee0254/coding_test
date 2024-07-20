########################################################################################
# sol 1)
########################################################################################
import sys

def dfs_bt(n, sm, cnt):
    global ans
    if n == N:
        if sm == S and cnt > 0:
            ans += 1
        return
    dfs_bt(n+1, sm + s_list[n], cnt+1)  # 포함하는 경우
    dfs_bt(n+1, sm, cnt)               # 포함하지 않는 경우

def main(N, S, s_list):
    global ans
    ans = 0
    dfs_bt(0, 0, 0)
    return ans
    
if __name__=="__main__":
    input = sys.stdin.readline
    N, S = map(int, input().strip().split())
    s_list = list(map(int, input().strip().split()))
    ret = main(N, S, s_list)
    print(ret)

########################################################################################
# sol 2) 실패 - 시간 초과
########################################################################################

# import sys

# def dfs_bt(n, lst):
#     if len(lst)!=0 and sum(lst) == S:
    
#     # if n == len(s_list):
#         ans.extend(lst)
#         return
    
#     for i in range(len(s_list)):
#         if vst[i] == 0:
#             vst[i] = 1
#             dfs_bt(n+1, lst+[s_list[i]])
#             vst[i] = 0
        
# def main(N, S):

#     global ans, vst
#     # lst = [] # 만들어진 경로 넣을 리스트
#     ans = [] # 최종 만들어진 경로들 리스트
#     vst = [0]*len(s_list) # 방문 노드 표시
    
#     tmp_path_list = []
#     for idx in range(len(s_list)):
#         dfs_bt(idx, [])
#         break
#     tmp_path_list.append(list(set(ans)))
#     print(tmp_path_list)
#     return len(tmp_path_list)
        
# if __name__=="__main__":
#     input = sys.stdin.readline
#     global s_list
#     N, S = map(int, input().strip().split())
#     old_s_list = list(map(int, input().strip().split()))
#     # for tmp_idx in range(len(s_list)):
#     #     if s_list[tmp_idx] == 0:
#     #         s_list.pop(tmp_idx)
#     s_list = []
#     for tmp_ele in old_s_list:
#         if tmp_ele != 0:
#             s_list.append(tmp_ele)
#     ret = main(N, S)
#     print(ret)
