n, p = map(int, input().split())
i = 0
backup = n
number = set()
for _ in range(100):
    n = (n*backup) % p
    i += 1
    if n in number:
        break
    number.add(n)
print(i-1)