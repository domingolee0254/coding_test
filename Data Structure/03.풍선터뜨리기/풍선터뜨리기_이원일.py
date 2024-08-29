import sys

def main(paper_list:list) -> list:
    result = []
    paper_list = [(i+1, paper_list[i]) for i in range(N)]
    current_index = 0

    while paper_list:
        b, p = paper_list.pop(current_index)
        result.append(b)

        if not paper_list:
            break

        if p > 0:
            current_index = (current_index + (p-1)) % len(paper_list)
        else:
            current_index = (current_index + p) % len(paper_list)

    return result

input = sys.stdin.readline
N = int(input().strip())
paper_list = list(map(int, input().strip().split()))
ret = main(paper_list)

print(*ret)