n = int(input())  
numbers = list(map(int, input().split())) 
numbers.sort(reverse=True)
total_sum = 0
for i in range(0, n, 3):
    group = numbers[i:i+3]  # 현재 묶음
    if len(group) == 3:  # 묶음이 3개일 경우
        total_sum += sum(group) - min(group)  # 가장 작은 값을 제외하고 합산
    else:  # 마지막 묶음 처리
        total_sum += sum(group)

print(total_sum)  # 결과 출력