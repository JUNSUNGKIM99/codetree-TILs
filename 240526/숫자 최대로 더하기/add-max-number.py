n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
B = arr[0]
for i in range(1, len(arr)):
    A = arr[i]
    B = B + (A/2)

print(B)