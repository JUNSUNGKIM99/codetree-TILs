def decrypt_substitution_cipher(encrypted_text, substitution_rule):
    # 생성할 복호화 맵
    decryption_map = {}
    
    # 치환 규칙을 통해 복호화 맵을 생성
    for i in range(26):
        decryption_map[substitution_rule[i]] = chr(ord('a') + i)
    
    print(decryption_map)
    # 복호화된 문자열 생성
    decrypted_text = ''
    for char in encrypted_text:
        if char == ' ':  # 띄어쓰기는 그대로 유지
            decrypted_text += ' '
        else:
            decrypted_text += decryption_map[char]
    
    return decrypted_text

def main():
    # 첫 번째 줄: 암호화된 문자열
    encrypted_text = input()
    
    # 두 번째 줄: 치환 규칙
    substitution_rule = input()
    
    # 복호화된 문자열을 구해서 출력
    decrypted_text = decrypt_substitution_cipher(encrypted_text, substitution_rule)
    print(decrypted_text)

if __name__ == "__main__":
    main()