tmp = input()
word = input()
position = []

for i in range(len(word)-1):
    if tmp.find(word[i]) < tmp.find(word[i+1]):
        position.append(1)
    else:
        position.append(0)
answer = 1
for p in position:
    if p == 0:
        answer += 1

print(answer)