n = int(input())
string = []
for _ in range(n):
    string.append(input())
string = ''.join(string)
print(string[:int(len(string)/2)])
print(string[int(len(string)/2):])