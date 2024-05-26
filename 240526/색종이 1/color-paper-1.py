def calculate_blue_area(n, coordinates):
    # 100x100 크기의 그리드를 0으로 초기화합니다.
    grid = [[0] * 100 for _ in range(100)]

    # 각 색종이의 위치를 그리드에 표시합니다.
    for x, y in coordinates:
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                grid[i][j] = 1

    # 1로 표시된 셀의 수를 셉니다.
    blue_area = sum(sum(row) for row in grid)
    
    return blue_area

# 입력 받기
n = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(n)]

# 파란색 영역의 넓이 계산 및 출력
result = calculate_blue_area(n, coordinates)
print(result)