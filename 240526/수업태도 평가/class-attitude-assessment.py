def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    # 첫 줄에서 N을 읽습니다.
    N = int(data[0])
    
    # 학생들의 이름과 초기 점수 설정
    students = {
        "Bessie": 0,
        "Elsie": 0,
        "Daisy": 0,
        "Gertie": 0,
        "Annabelle": 0,
        "Maggie": 0,
        "Henrietta": 0
    }
    
    # 점수 부여 정보를 처리합니다.
    for i in range(1, N + 1):
        name, score = data[i].split()
        score = int(score)
        students[name] += score
    
    # 점수를 기준으로 학생을 정렬합니다.
    sorted_scores = sorted(students.items(), key=lambda x: x[1])
    
    # 두 번째로 낮은 점수를 찾습니다.
    lowest_score = sorted_scores[0][1]
    second_lowest_score = None
    
    for score in sorted_scores:
        if score[1] > lowest_score:
            second_lowest_score = score[1]
            break
    
    # 두 번째로 낮은 점수를 가진 학생들을 찾습니다.
    if second_lowest_score is None:
        print("Tie")
        return
    
    second_lowest_students = [student for student, score in sorted_scores if score == second_lowest_score]
    
    # 결과 출력
    if len(second_lowest_students) == 1:
        print(second_lowest_students[0])
    else:
        print("Tie")

if __name__ == "__main__":
    main()