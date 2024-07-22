def solution(edges):
    def count_edges(edges):
        edge_counts = {}
        for a, b in edges:
            # 각 노드를 키로, 밸류를 간선의 수로 하여 추가할 딕셔너리 생성
            # .get() 함수를 이용해 딕셔너리의 키 값 추가
            if not edge_counts.get(a):
                edge_counts[a] = [0, 0]
            
            if not edge_counts.get(b):
                edge_counts[b] = [0, 0]
                
            # output edge와 input edge의 개수를 추가
            edge_counts[a][0] += 1 # a는 n번 노드에서 나가는 간선
            edge_counts[b][1] += 1 # b는 n번 노드로 들어오는 간선
        
        return edge_counts

    # 어려운 부분: 각 그래프를 수를 구하는 과정
    def check_answer(edge_counts):
        answer = [0, 0, 0, 0]
        for key, counts in edge_counts.items():
            # 생성된 정점의 번호 확인
            if counts[0] >= 2 and counts[1] == 0:
                answer[0] = key
            # 막대 모양 그래프의 수 확인
            elif counts[0] == 0 and counts[1] > 0:
                answer[2] += 1
            # 8자 모양의 그래프의 수 확인
            elif counts[0] >= 2 and counts[1] >= 2:
                answer[3] += 1
            
        # 도넛 모양 그래프의 수 확인
        answer[1] = (edge_counts[answer[0]][0] - answer[2] - answer[3])
        
        return answer
    
    edge_counts = count_edges(edges)
    answer = check_answer(edge_counts)
    
    return answer

if __name__=="__main__":
    edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
    ret = solution(edges)
    print(ret)
