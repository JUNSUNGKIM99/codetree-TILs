def expand_grid(N, M, K, grid):
    for row in grid:
        for _ in range(K):
            print(''.join(row * K))

def main():
    N, M, K = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(input())

    expand_grid(N, M, K, grid)

if __name__ == "__main__":
    main()