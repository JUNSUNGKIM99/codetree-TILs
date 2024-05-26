n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for a in arr:
    if m >= a:
        m += 1
    else:
        break
    
print(m)