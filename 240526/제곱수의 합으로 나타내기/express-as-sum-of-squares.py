import math

def min_square_sum(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = i  # 초기값 설정
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[i - j*j] + 1)  # 동적 계획법을 이용하여 최소값 갱신
    return dp[n]

n = int(input())  # 자연수 n 입력
print(min_square_sum(n))  # 결과 출력