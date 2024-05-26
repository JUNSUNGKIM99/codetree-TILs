a, b = input().split()
tmp1 = ""
tmp2 = ""
for _ in a:
    if _.isalpha():
        pass
    else:
        tmp1 += _
for _ in b:
    if _.isalpha():
        pass
    else:
        tmp2 += _

print(int(tmp1)+int(tmp2))