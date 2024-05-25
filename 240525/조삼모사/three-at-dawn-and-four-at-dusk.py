import sys 

INT_MAX = sys.maxsize

n = int(input())
p = [
    list(map(int, input().split()))
    for _ in range(n)
]
evening = [
    False for _ in range(n)
]

ans = INT_MAX
#아침과 저녁 간의 힘듦의 차이를 계산합니다. 
def calc():
    morning_sum = sum([
        p[i][j]
        for i in range(n)
        for j in range(n)
        if not evening[i] and not evening[j]
    ])
    evening_sum = sum([
        p[i][j]
        for i in range(n)
        for j in range(n)
        if evening[i] and evening[j]
    ])

    return abs(morning_sum - evening_sum)

def find_min(curr_idx, cnt):
    global ans

    if cnt == n // 2:
        ans = min(ans, calc())
        return
    
    if curr_idx == n:
        return
    
    find_min(curr_idx+1, cnt)
    evening[curr_idx] = True
    find_min(curr_idx+1, cnt+1)
    evening[curr_idx] = False

find_min(0,0)
print(ans)