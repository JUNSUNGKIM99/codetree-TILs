N = int(input())

def fibonacci(n) :
    if n == 0 :
        return n
    a, b = 0, 1 # 초깃값 두 수 
    for i in range (1, N) :
        temp= a
        a = b
        b= temp+a
    return b

print(fibonacci(N))