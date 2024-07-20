import sys

def dfs_bt(n):
    global ans
    if n == N:
        ans += 1
        return
    
    for j in range(N): # 열
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n+j] = v3[n-j]= 1
            dfs_bt(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0 
    
def main(N):
    
    global v1, v2, v3, ans
    v1 = [0]*N
    v2 = [0]*(2*(N-1))
    v3 = [0]*(2*(N-1))
    ans = 0
    
    dfs_bt(0)

    return ans

if __name__=='__main__':
    input = sys.stdin.readline
    N = int(input().strip())
    ret = main(N)
    print(ret)

# 프로그래머스 예시
# def solution(n, queries):
#     answer = []
#     return answer
# 프로그래머스처럼 연습하려면 
# __main__ 스페이스에서 변수 선언해서 글로벌 변수처럼 사용하는 거 하지 말아야겠음