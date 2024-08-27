import sys

def main() -> list:
    frames = []  # 사진틀에 들어있는 학생들
    recommendation_count = {}  # 학생별 추천 횟수

    for student in stu_list:
        if student in recommendation_count:
            # 이미 사진틀에 있는 학생이면 추천 횟수만 증가
            recommendation_count[student] += 1
        else:
            if len(frames) < N:
                # 사진틀에 빈 자리가 있으면 추가
                frames.append(student)
                recommendation_count[student] = 1
            else:
                # 사진틀에 빈 자리가 없으면 교체해야 함
                # 가장 적게 추천받은 학생을 찾기
                min_recommend = min(recommendation_count.values())
                candidates = [s for s in frames if recommendation_count[s] == min_recommend]
                
                # 가장 적게 추천받은 학생 중 가장 오래된 학생을 제거
                student_to_remove = candidates[0]
                frames.remove(student_to_remove)
                del recommendation_count[student_to_remove]
                
                # 새로운 학생을 사진틀에 추가
                frames.append(student)
                recommendation_count[student] = 1
    
    # 최종 후보 학생들을 번호 순서대로 정렬하여 반환
    return sorted(frames)

input = sys.stdin.readline    
N = int(input().strip())
num = int(input().strip())
stu_list = list(map(int, input().strip().split()))

ret = main()
print(' '.join(map(str, ret)))