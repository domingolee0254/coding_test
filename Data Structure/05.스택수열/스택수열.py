import sys

def main():
    stack = []
    result = []
    current = 1

    for number in sequence:
        # 현재 수열의 숫자에 도달할 때까지 스택에 숫자를 push
        while current <= number:
            stack.append(current)
            result.append('+')
            current += 1
        
        # 스택의 최상단 값 == 현재 수열의 숫자와 같다면 pop
        if stack and stack[-1] == number:
            stack.pop()
            result.append('-')
        else:
            return ["NO"]
    
    return result

input = sys.stdin.readline
N = int(input().strip())
sequence = [int(input().strip()) for _ in range(N)]
output = main()

print('\n'.join(output))
