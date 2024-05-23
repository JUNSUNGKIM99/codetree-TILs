def remove_char_at_index(s, index):
    return s[:index - 1] + s[index:]

def main():
    a, n = input().split()
    n = int(n)

    for _ in range(n):
        index = int(input())
        if index <= len(a):
            a = remove_char_at_index(a, index)
            print(a)

if __name__ == "__main__":
    main()