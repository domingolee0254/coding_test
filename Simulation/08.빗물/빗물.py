import sys

def main(H:int, W:int, blocks:list) -> list:
    
    ans = 0
    for i in range(1, W-1): # 왜 1부터지? 2부터여야 하는 거 아닌가? 첫번째 칸이 1이잖음
        # W의 개수가 1부터지, 첫번째 칸의 인덱스는 0부터임. w=4일때 0, 3은 버리면 => 1:w-2  
        left_max = max(blocks[:i])
        right_max = max(blocks[i+1:])
        
        compared_min = min(left_max, right_max)
        
        if blocks[i] < compared_min:
            ans += compared_min - blocks[i]
            
    return ans
        
if __name__=="__main__":
    input = sys.stdin.readline
    H, W = map(int, input().strip().split())
    blocks = list(map(int, input().strip().split()))
    ret = main(H, W, blocks)
    print(ret)