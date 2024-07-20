def reconstruct_inorder_traversal(K, inorder):
    # 트리의 노드 수 및 각 레벨의 노드 수 계산
    num_nodes = (2**K) - 1  # 2^K - 1
    level_indices = [(1**i) - 1 for i in range(K+1)]  # 각 레벨의 시작 인덱스
    
    # 각 노드의 레벨 결정을 위한 배열
    levels = [0] * num_nodes

    # 중위 순회를 재구성하는 함수
    def place_inorder(start, end, level):
        if start > end:
            return
        mid = (start + end) // 2
        levels[mid] = level
        place_inorder(start, mid - 1, level + 1)
        place_inorder(mid + 1, end, level + 1)

    # 중위 순회 시작
    place_inorder(0, num_nodes - 1, 0)

    # 결과를 레벨별로 저장하기 위한 리스트
    result = [[] for _ in range(K)]

    # 방문 순서대로 레벨에 맞게 배치
    for idx, node in enumerate(inorder):
        node_index = levels[idx]  # 노드 번호로 해당 레벨 인덱스를 찾음
        result[node_index].append(node)

    return result

if __name__ == '__main__':
    K = int(input().strip())
    inorder_list = list(map(int, input().strip().split()))
    ret = reconstruct_inorder_traversal(K, inorder_list)
    
    for level_nodes in ret:
        print(' '.join(map(str, level_nodes)))
