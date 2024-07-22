import sys

def main(N:int, num:int, stu_list:list) -> list:
    result = []  # 사진틀에 있는 학생들의 리스트
    cnt = []  # 각 학생의 추천 횟수를 저장하는 리스트

    for i in stu_list:
        if i in result:
            cnt[result.index(i)] += 1  # 이미 사진틀에 있는 학생이면 추천 횟수 증가
        else:
            if len(result) >= N:  # 사진틀이 가득 찼으면
                idx = cnt.index(min(cnt))  # 최소 추천 횟수를 가진 학생 찾기
                                           # 다 같은 최소 값이면 가장 먼저들어온게 사라져서 어차피 가장 오래된 날짜의 것이 사라짐 
                del result[idx]  # 해당 학생 제거
                del cnt[idx]  # 해당 학생의 추천 횟수 제거
            result.append(i)  # 새 학생 추가
            cnt.append(1)  # 새 학생의 추천 횟수 초기화

    result.sort()  # 최종 후보 학생 번호를 오름차순으로 정렬
    return result

if __name__ == "__main__":
    input = sys.stdin.readline    
    N = int(input().strip())
    num = int(input().strip())
    stu_list = list(map(int, input().strip().split()))
    ret = main(N, num, stu_list)
    print(' '.join(map(str, ret)))
