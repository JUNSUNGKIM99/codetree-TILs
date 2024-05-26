def min_flips_to_make_uniform(S):
    count_0_groups = 0
    count_1_groups = 0
    # 첫 번째 문자의 그룹을 먼저 셉니다.
    if S[0] == '0':
        count_0_groups += 1
    else:
        count_1_groups += 1
    # 문자열을 순회하며 그룹의 변화를 셉니다.
    for i in range(1, len(S)):
        if S[i] != S[i-1]: #애초에 바로 앞 숫자가 다르다,
        #다르면 이제, 지금 나오는게 0이면 0그룹 추가하고, 1이면 1그룹 추가
            if S[i] == '0':
                count_0_groups += 1
            else:
                count_1_groups += 1
    
    return min(count_0_groups, count_1_groups)

S = input().strip()

# 결과 계산 및 출력
result = min_flips_to_make_uniform(S)
print(result)