s = []
comp = []
for i in range(28):
    n = int(input())
    s.append(n)
for i in range(30):
    comp.append(i+1)

for i in range(28):
    if s[i] in comp:
        comp.remove(s[i])
print(min(comp))
print(max(comp))