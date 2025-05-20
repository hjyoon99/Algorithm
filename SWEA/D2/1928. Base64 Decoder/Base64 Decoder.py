def base64_decode_manual(encoded_str):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_map = {c: i for i, c in enumerate(base64_chars)}

    # 패딩 제거
    padding = encoded_str.count('=')
    encoded_str = encoded_str.rstrip('=')

    # 6비트 단위로 숫자 추출
    bitstream = ""
    for char in encoded_str:
        val = base64_map[char]
        bitstream += format(val, '06b')

    # 8비트 단위로 잘라서 바이트로 변환
    bytes_list = []
    for i in range(0, len(bitstream) - padding * 8, 8):
        byte = int(bitstream[i:i+8], 2)
        bytes_list.append(byte)

    return bytes(bytearray(bytes_list)).decode('utf-8')

t = int(input())
for test_case in range(1, t+1):
    string = input()

    print(f'#{test_case} {base64_decode_manual(string)}')
