import sys

def main(N:int, D:int, short_cuts:list)->int:
    dist = [i for i in range(D+1)] # hp1 = 왜 D+1 까지 인가

    for i in range(D+1):
        # 지름길 안타는 경우(아래 for문에서 업데이트 한 거리를 반영해서 직진할 때랑 비교)
        if i > 0: # 어차리 dist[0]은 0으로 초기화되어있의니 상관무
            dist[i] = min(dist[i], dist[i-1]+1)
        
        # 지름길을 사용하는 경우  
        for start_idx, end_idx, length in short_cuts:
            if start_idx >= 0 and end_idx <= D: # 
                dist[end_idx] = min(dist[end_idx], dist[start_idx] + length) # hp2 = update해주는 부분 
                
    return int(dist[D])

if __name__=="__main__":
    input = sys.stdin.readline
    N, D = map(int, input().strip().split())
    short_cuts = [list(map(int, input().strip().split())) for i in range(N)]
    
    ret = main(N, D, short_cuts)
    print(ret)
    
    

# for i in range(D+1): # hp3 = 왜 D까지 인가 
#     if i%100==0:
#         print(i)
#     dist[i+1] = min(dist[i+1], dist[i]+1)
# 이렇게 하면 인덱스 에러 dist[i+1] dist[901] 저장할 공간없음 