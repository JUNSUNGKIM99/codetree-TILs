n, p = map(int, input().split())
i = 0
backup = n
number = set() 
while True:
    n = (n*backup) % p
    #print(i, n, number)
    if n not in number:
        number.add(n)
        i += 1
    else:
        break
print(i-1)