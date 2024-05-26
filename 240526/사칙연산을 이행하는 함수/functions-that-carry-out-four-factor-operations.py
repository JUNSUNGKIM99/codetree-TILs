a,op,b = input().split()

def oper(a,op,b):
    if op == '+':
        print("{} {} {} = {}".format(a,op,b,int(a)+int(b)))
    elif op == '-':
        print("{} {} {} = {}".format(a,op,b,int(a)-int(b)))
    elif op == '*':
        print("{} {} {} = {}".format(a,op,b,int(a)*int(b)))
    elif op == '/':
        print("{} {} {} = {}".format(a,op,b,int(int(a)/int(b))))
    else:
        return

oper(a,op,b)