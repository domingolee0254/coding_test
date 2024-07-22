# key idea: 1. 시퀀스 데이터를 탐색한다 => 트리나 트라이 구조
#           2. 근데 문자열들이 반복되거나 비슷한 게 많네 => 시간복잡도가 적은 트라이 구조로 가자
# process: 1. trie 선언
# process: 2. 탐색시 비교대상이 될 db 문자열(S에 포함된 문자열) 삽입
#          2-1) 트라이 한 노드에 한 문자열 넣어서 시퀀스대로 타고타고 들어가기
#          2-2) 노드가 다시 child 노드 부르는 식
#          2-3) 문자열 끝나면 끝임을 표시
# process: 3. 탐색 대상이 될 쿼리 문자열과 db 문자열 비교 및 검색 후 cnt 추가

import sys

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode() # root 노드 선언
    
    def insert(self, db_word:str):
        curr_node = self.root # 특정 노드를 기준으로 child를 타고타고 들어갈 거니까 현재노드를 루트로 초기화
        for char in db_word:
            if char not in curr_node.children: # 현재 문자 "A"가 딕셔너리에 없다면
                curr_node.children[char] = TrieNode() # children이라는 거 자체가 그 노드가 물고있는 딕셔너리이므로
                                                  #'A'라는 키 값을 만들고(자식노드) 클래스를 만들어 넣음(A의 자식도 다른 자식을 물거니까)
            # char가 children에 이미 있으면 
            curr_node = curr_node.children[char] # A의 자식노드를 새 루트로 삼고 다시 파고들기 
        curr_node.end_of_word = True # word 문자열이 다 끝났다는 표시 (A-P-P-L-E)
        
    def search(self, q_word:str):
        curr_node = self.root # 검색 하는 것도 마찬가지로 파고들면서 문자열이 다 매칭되는 지 보니까 같은 원리
        for char in q_word:
            if char not in curr_node.children:
                return False # 문자열이 1개라도 틀리면 main함수의 search에서 if False가 되도록 - 그래야 cnt가 추가안됨
            curr_node = curr_node.children[char] # 차일드 노드로 이동
        return curr_node.end_of_word # 하나도 틀림 없이 끝까지 다맞으면 원래 끝에 있던 True 반환
        

def main(db_list, query_list):
    
    # 트라이 선언 
    trie = Trie()
    
    # 데이터 입력
    for db_word in db_list:
        # 트라이.insert 함수 실행 -> 문자열 삽입
        trie.insert(db_word)
    
    # 데이터 검색
    cnt = 0 
    for j in query_list:
        # 트라이.search 함수 실행 -> 검색 되는 개수 세기 
        if trie.search(j):
            cnt += 1

    return cnt

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().strip().split())
    db_list = [input().strip() for _ in range(N)]
    query_list = [input().strip() for _ in range(M)]
    
    ret = main(db_list, query_list)
    print(ret)
