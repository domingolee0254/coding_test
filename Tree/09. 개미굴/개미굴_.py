# idea : 디렉토리 구조 같다 , 트라이 + dfs(재귀)
# 트라이가 맞음. 갈래갈래로 갈라지므로 원리가 문자열 트라이와 비슷
# 입력이 키위, 애플로 시작하고 이거는 생태학에서랑 비슷(루트가 있으면 거기에서 다른 췰드런 붙여가면서 시작)
# node 초기화할 때 node.children, node.is_end =T/F, node.level 설정
# 재귀로 끝까지 가고 end 이면 그때까지의 레벨과, 경로 출력 
# ABCD이면 마지막 'D'빼고 앞에 문자열 1개 당 '--'으로 교체

import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.level = 0
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # node 정보 넣어주기
    def insert(self, foods):
        current = self.root
        for fd in foods:
            if fd not in current.children:
                current.children[fd] = TrieNode()
            current = current.children[fd]
            current.level += 1
        current.is_end = True
    
    # 프린트 먹이 정보를 리스트에 순서대로 넣어주는 함수
    def make_chain(self, foods):
        foods_chain = []
        # dfs에서 리턴된 문자열 삽입
        foods_chain.append(dfs())       
        # 그것을 거꾸로 정렬
        pass
    
    def _dfs(self, foods):
        if 
        # end 가 아니라면 child 파고들기
        # end라면 그때의 food 리턴 - 문자열
        pass
    
    
def main(ant_hole_info_list):
    food_trie = Trie()
    
    # 음식을 트라이에 삽입 
    for foods in ant_hole_info_list:  #food_infos = APPLE BANANA KIWI
        food_trie.insert(foods[1:])
    
    # 만들어진 트라이에서 경로를 만들기
    food_trie.make_chain()
        
        
    return tmp

if __name__=="__main__":
    input = sys.stdin.readline
    N = int(input().split())
    ant_hole_info_list = [input().strip().split() for _ in range(N)]
    ret = main(ant_hole_info_list)
    