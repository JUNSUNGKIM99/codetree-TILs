def min_sum_removal(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] + arr[1]
    
    # DP 배열 초기화
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = min(dp[1] + arr[2], arr[0] + arr[1] + arr[2] - min(arr[0], arr[1], arr[2]))
    
    # DP 테이블 채우기
    for i in range(3, n):
        case1 = dp[i-1] + arr[i]
        case2 = dp[i-2] + arr[i-1] + arr[i]
        case3 = dp[i-3] + arr[i-2] + arr[i-1] + arr[i] - min(arr[i-2], arr[i-1], arr[i])
        dp[i] = min(case1, case2, case3)
    
    return dp[-1]

# 입력 받기
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# 결과 계산 및 출력
print(min_sum_removal(arr))