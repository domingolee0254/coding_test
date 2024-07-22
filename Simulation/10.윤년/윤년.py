import sys

input = sys.stdin.readline

n = int(input().strip())

if n % 4 == 0 and n % 100 != 0:
    print(1)
# 처음에 한짓
#elif n % 4 == 0 and n % 100 != 0 and n % 400 == 0 :
# 아니 400의 배수인데 100의 배수가 어떻게 아닐 수 있어, 문제 이해를 잘하자
# 변수들의 범위를 잘 고려해야한다
elif n % 4 == 0 and n % 100 == 0 and n % 400 == 0 :

    print(1)
else:
    print(0)


