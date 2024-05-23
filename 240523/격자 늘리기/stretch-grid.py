n, m, k = map(int, input().split())
text = []
for _ in range(n):
    text.append(input())

for t in text:
    for _ in range(k):
        for char in t:
            print(char*k,end='')
        print(' ')