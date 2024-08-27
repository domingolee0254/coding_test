### 시간 초과
# 1. deque
# 2. popleft
# 3. sys.stdout.write("\n".join(map(str, rets)) + "\n")
# 4. pypy3 pass, python3 fail

import sys
from collections import deque

def main() -> list:
    # queue = [] 
    queue = deque()
    results = []

    for command in commands:
        if command[0] == 'push':
            queue.append(command[1])
        elif command[0] == 'pop':
            if len(queue) != 0:
            #    results.append(queue.pop(0))
                results.append(queue.popleft())
            else:
               results.append(-1)
        elif command[0] == 'size':
            results.append(len(queue))
        elif command[0] == 'empty':
            if len(queue) != 0:
               results.append(0)
            else:
                results.append(1)
        elif command[0] == 'front':
            if len(queue) != 0:
               results.append(queue[0])
            else:
                results.append(-1)
        elif command[0] == 'back':
            if len(queue) != 0:
               results.append(queue[-1])
            else:
                results.append(-1)
        else:
            pass
    return results

input = sys.stdin.readline
N = int(input().strip())
commands = [input().strip().split(' ')  for _ in range(N)]

rets = main()

sys.stdout.write("\n".join(map(str, rets)) + "\n")