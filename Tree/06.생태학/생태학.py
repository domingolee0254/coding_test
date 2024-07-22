###################################################################
# Trie + DFS
###################################################################
import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_species = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, species):
        current_node = self.root
        for char in species:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.end_of_species = True
        current_node.count += 1
    
    def calculate_percentages(self, total_count):
        results = []
        self._dfs(self.root, "", results, total_count)
        return results
    
    def _dfs(self, node, prefix, results, total_count):
        if node.end_of_species:
            percentage = (node.count / total_count) * 100
            results.append(f"{prefix} {percentage:.4f}")
        for char in sorted(node.children.keys()):
            self._dfs(node.children[char], prefix + char, results, total_count)

def main(trees:list):
    trie = Trie()
    total_trees = 0
    
    for tree in trees:
        trie.insert(tree)
        total_trees += 1
    
    results = trie.calculate_percentages(total_trees)

    return results

if __name__ == "__main__":
    input = sys.stdin.readline
    trees = []
    while True:
        line = input().strip()
        if line == '':
            break
        trees.append(line)

    # Again, to run this in a script you would call:
    ret = main(trees)
    print("\n".join(ret))



###################################################################
# 실패 Counter 방식(백준 테스트 케이스는 되는데 다른 케이스는 안됨)
###################################################################
# import sys
# from collections import Counter

# def main(in_list):
    
#     total_num = len(in_list)
#     tmp_dict = {}
     
#     tmp = Counter(in_list)
#     for k in tmp:
#         tmp_dict[k] = round((tmp[k] / total_num) * 100, 4)
#     final_dict = sorted(tmp_dict.items())
    
#     return final_dict

# if __name__ == "__main__":
#     input = sys.stdin.readline
#     in_list = []
#     while True:
#         line = input().strip()
#         if line == '':
#             break
#         in_list.append(line)

#     ret = main(in_list)
    
#     # 출력 형식 변경
#     for key, value in ret:
#         print(f"{key} {value}")  # 키와 밸류를 공백으로 구분

