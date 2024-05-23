s = input()

for _ in range(len(s)+1):
    print(s)
    s = s[1:] + s[0]