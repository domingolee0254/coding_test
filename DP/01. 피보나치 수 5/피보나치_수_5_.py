# 피보나치 수 2.py에서 0과 1을 따로 처리

import sys

def main(n:int) -> int: #type hinting
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:    
        F_list = [0, 1]
        for i in range(1, n):
            F_list.append(F_list[i-1] + F_list[i])

        return F_list[-1]

if __name__ == '__main__':
    
    input = sys.stdin.readline
    n = int(input().strip())
    ret = main(n)
    print(ret)
    