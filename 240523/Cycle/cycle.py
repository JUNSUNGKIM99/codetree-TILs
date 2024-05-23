def find_cycle_size(N, P):
    visited = {}  # 이미 방문한 숫자를 저장하기 위한 딕셔너리
    current = N   # 시작 숫자

    count = 0     # 반복 횟수 카운트
    while current not in visited:
        visited[current] = count  # 현재 숫자와 반복 횟수 저장
        count += 1
        # 현재 숫자를 key로 하고 count를 value로 가지고있으면, 다음에 만날때 빼면됨...
        # 다음 숫자 계산
        next_num = (current * N) % P
        current = next_num

    return count - visited[current]  # 사이클의 크기 반환

def main():
    N, P = map(int, input().split())
    cycle_size = find_cycle_size(N, P)
    print(cycle_size)

if __name__ == "__main__":
    main()