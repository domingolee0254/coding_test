# key idea: 1. 중심 노드를 정하고, 이 노드에 노드들을 연결
#           2. 중심 노드에 리프 노드 1개 추가(트리의 구조를 간단하고 명확하게 유지하기 위함, 조정하기 편함)
# 왜 중심노드를 한 개 정하고, 0 노드 1개를 붙이지? 2개 3개를 붙일 수는 없나? => 복잡해짐

import sys

def main(n, m): # n = 5, m = 3
    edges = []
    # 노드 1을 중심 노드로 설정하고 이 노드에 노드 2부터 m까지 연결하여 리프를 만듦
    for i in range(2, m + 1):
        edges.append((1, i))
    # 노드 0을 노드 1에 연결하여 노드 1이 리프가 되지 않도록 함
    edges.insert(0, (0, 1))
    
    # 위에서 연결되지 않은 나머지 노드들을 연결
    if m + 1 <= n - 1: # m: 리프 노드의 개수, m+1: 리프 노드 다음으로 처리할 노드의 인덱스
                       # n: 트리 전체의 노드의 개수, n-1은 마지막 노드의 인덱스(노드0 시작 하니까)
        # 마지막으로 생성된 리프 노드부터 시작하여 나머지 노드들을 연결
        last_node = m
        for i in range(m + 1, n):
            edges.append((last_node, i))
            last_node = i

    return edges

if __name__=='__main__':
    input = sys.stdin.readline
    n, m = map(int, input().strip().split()) # n = node, m = leaf
    ret = main(n, m)

    for edge in ret:
        print(edge[0], edge[1])
