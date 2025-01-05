def solution(today, terms, privacies):
    result = []
    # 오늘 날짜 분리
    today_y, today_m, today_d = map(int, today.split("."))

    # 약관 종류와 유효기간 딕셔너리 생성
    term_dict = {}
    for term in terms:
        kind, months = term.split()
        term_dict[kind] = int(months)

    # 개인정보 유효기간 확인
    for idx, privacy in enumerate(privacies):
        pri_date, pri_kind = privacy.split()
        pri_y, pri_m, pri_d = map(int, pri_date.split("."))
        
        # 약관에 따라 유효기간 추가
        add_months = term_dict[pri_kind]
        pri_m += add_months
        
        # 월이 12를 넘으면 연도로 환산
        pri_y += (pri_m - 1) // 12
        pri_m = (pri_m - 1) % 12 + 1  # 1월부터 12월까지 범위로 조정
        pri_d -= 1  # 하루 전날까지 유효
        
        if pri_d == 0:  # 만약 일자가 0이 되면 한 달 전으로 조정
            pri_m -= 1
            pri_d = 28
            if pri_m == 0:
                pri_m = 12
                pri_y -= 1

        # 유효기간과 오늘 날짜 비교
        if (pri_y < today_y or 
            (pri_y == today_y and pri_m < today_m) or 
            (pri_y == today_y and pri_m == today_m and pri_d < today_d)):
            result.append(idx + 1)  # 인덱스는 1부터 시작

    return result