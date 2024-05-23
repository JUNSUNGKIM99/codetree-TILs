a, b = map(int, input().split())

for i in range(1, 10):
    print("{} * {} = {} {} * {} = {}".format(a,i,a*i,b,i,b*i))