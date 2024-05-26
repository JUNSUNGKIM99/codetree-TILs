def remove_word_from_string(s, word):
    while word in s:
        s = s.replace(word, '', 1)  # 단어를 한 번만 제거합니다.
    return s

def main():
    # 첫 번째 줄: 입력 문자열
    input_string = input().strip()
    
    # 두 번째 줄: 삭제할 단어
    word_to_remove = input().strip()
    
    # 결과를 계산하여 출력
    result = remove_word_from_string(input_string, word_to_remove)
    print(result)

if __name__ == "__main__":
    main()