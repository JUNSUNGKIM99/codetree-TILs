n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
k = 1
for i in range(n):
    for j in range(n):
        arr[j][i] = k
        k += 1
    
for a in arr:
    print(a)