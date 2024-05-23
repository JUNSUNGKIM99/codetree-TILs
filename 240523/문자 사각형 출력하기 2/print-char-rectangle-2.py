def print_square(n):
    # 알파벳 리스트 생성
    alphabet = [chr(ord('A') + i) for i in range(26)]
    # 출력할 격자 생성
    grid = [[' ' for _ in range(n)] for _ in range(n)]

    # 문자 채우기
    char_index = 0
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                grid[i][j] = alphabet[char_index]
                char_index = (char_index + 1) % 26
            else:
                grid[i][n - 1 - j] = alphabet[char_index]
                char_index = (char_index + 1) % 26

    # 격자 출력
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=' ')
        print()
    
def main():
    n = int(input())
    print_square(n)

if __name__ == "__main__":
    main()