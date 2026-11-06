from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    t1 = []
    t2 = []
    
    # 2. 첫 번째 문자열 2글자씩 끊기 + 알파벳인 경우만 추가
    for i in range(len(str1) - 1):
        pair = str1[i:i+2]
        if pair.isalpha():  # 둘 다 알파벳(문자)인 경우만
            t1.append(pair)
            
    # 3. 두 번째 문자열도 독립적으로 반복문 실행!
    for i in range(len(str2) - 1):
        pair = str2[i:i+2]
        if pair.isalpha():
            t2.append(pair)
    
    c1 = Counter(t1)
    c2 = Counter(t2)
    
    intersection = sum((c1 & c2).values()) # 교집합 총 개수
    union = sum((c1 | c2).values())       # 합집합 총 개수
    
    if union == 0:
        return 65536
    
    return int((intersection / union) * 65536)