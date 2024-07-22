import sys

def main(n:int, F_list:list) -> int: #type hinting
    for i in range(1, n):
        F_list.append(F_list[i-1] + F_list[i])

    return F_list[-1]

if __name__ == '__main__':
    
    input = sys.stdin.readline
    n = int(input().strip())
    F_list = [0, 1]
    ret = main(n, F_list)
    print(ret)
    