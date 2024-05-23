n, p = map(int, input().split())
i = 0
backup = n
number = set() 
while True:
    n = (n*backup) % p
    if n in number:
        i -= 1
        break
    number.add(n)
    i += 1
    
print(i)