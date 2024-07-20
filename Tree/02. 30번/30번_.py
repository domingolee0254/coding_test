import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_path = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, path):
        node = self.root
        for bit in path:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.is_end_of_path = True
    
    def find_lca(self, path_a, path_b):
        node = self.root
        lca_path = ''
        # Traverse the trie with both paths until they diverge
        for bit_a, bit_b in zip(path_a, path_b):
            if bit_a != bit_b or bit_a not in node.children:
                break
            lca_path += bit_a
            node = node.children[bit_a]
        
        # Convert the binary path back to the node number
        return int(lca_path, 2) if lca_path else None

# Helper function to get the binary path for a given node number
def get_binary_path(node_number):
    print(node_number)
    print(bin(node_number))
    print()
    return bin(node_number)[2:]


# Process the test cases using the trie to find the lowest common ancestor
def main(test_cases):

    # Initialize a trie and insert all paths for the given range
    trie = Trie()
    for i in range(1, 1024):
        path = get_binary_path(i)
        trie.insert(path)
    
    # Process the given test cases
    answers = []
    for a, b in test_cases:
        path_a = get_binary_path(a)
        path_b = get_binary_path(b)
        lca = trie.find_lca(path_a, path_b)
        answers.append(lca)    
    final_answers = [(x * 10) for x in answers]
    
    return final_answers

if __name__=="__main__":
    input = sys.stdin.readline
    T = int(input().strip())
    # 집합 S에 포함된 문자열들
    test_cases = [list(map(int, input().strip().split())) for _ in range(T)]
    
    ret = main(test_cases)
    print(*ret)