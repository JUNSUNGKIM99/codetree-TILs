n = int(input())
customers = list(map(int, input().split()))
lead, member = map(int, input().split())

people = 0

for i in range(n):
    customers[i] -= lead
    people += 1
    
    if customers[i] < 0:
        continue
    elif customers[i] > 0:
        people += customers[i] // member
        if customers[i] % member != 0:
            people += 1
        else:
            pass




print(people)