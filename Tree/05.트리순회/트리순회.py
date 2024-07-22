import sys

class Node:
    def __init__(self, root_node, left_node=None, right_node=None):
        self.root_node = root_node
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node):
    if node is None:
        return
    # 루트 노드 출력
    print(node.root_node, end='')
    # 왼쪽 자식 노드 순회
    if node.left_node:
        pre_order(Binary_tree[node.left_node])
    # 오른쪽 자식 노드 순회
    if node.right_node:
        pre_order(Binary_tree[node.right_node])

def in_order(node):
    if node is None:
        return
    if node.left_node:
        in_order(Binary_tree[node.left_node])
    print(node.root_node, end='')
    if node.right_node:
        in_order(Binary_tree[node.right_node])

def post_order(node):
    if node is None:
        return
    if node.left_node:
        post_order(Binary_tree[node.left_node])
    if node.right_node:
        post_order(Binary_tree[node.right_node])
    print(node.root_node, end='')

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input().strip())  # 노드의 개수를 읽음
    
    Binary_tree = {}
    
    for tmp_idx in range(N):
        nodes = sys.stdin.readline().strip()
        root_node, left_node, right_node = nodes.split()
        if tmp_idx == 0:
            init_root = root_node
        if left_node == '.':
            left_node = None
        if right_node == '.':
            right_node = None
        Binary_tree[root_node] = Node(root_node, left_node, right_node)

    root = Binary_tree[init_root]
    pre_order(root)
    print()
    in_order(root)
    print()
    post_order(root)
    print()

###############################################################################################
# import sys

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.nodes = {}
    
#     def add_node(self, value, left, right):
#         if value not in self.nodes:
#             self.nodes[value] = Node(value)
#         if left != '.':
#             self.nodes[left] = Node(left)
#             self.nodes[value].left = self.nodes[left]
#         if right != '.':
#             self.nodes[right] = Node(right)
#             self.nodes[value].right = self.nodes[right]
    
#     def preorder(self, node):
#         if node is None:
#             return ""
#         return node.value + self.preorder(node.left) + self.preorder(node.right)

#     def inorder(self, node):
#         if node is None:
#             return ""
#         return self.inorder(node.left) + node.value + self.inorder(node.right)
    
#     def postorder(self, node):
#         if node is None:
#             return ""
#         return self.postorder(node.left) + self.postorder(node.right) + node.value

# if __name__ == '__main__':
#     input = sys.stdin.readline
#     N = int(input().strip())  # 노드의 개수를 읽음

#     inputs = []
#     for _ in range(N):
#         line = input().strip()  # 각 노드와 자식 노드에 대한 정보를 읽음
#         inputs.append(line)  # 읽은 라인을 리스트에 추가

#     # 이진 트리 구성
#     bt = BinaryTree()
#     for line in inputs:
#         node, left, right = line.split()
#         bt.add_node(node, left, right)

#     # 순회 결과 출력
#     root = bt.nodes['A']
#     print(bt.preorder(root))
#     print(bt.inorder(root))
#     print(bt.postorder(root))
