def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)

    # 1️⃣ 여벌도 있고 도난도 당한 학생 제거
    common = lost & reserve
    lost -= common
    reserve -= common

    # 2️⃣ 체육복 빌려주기
    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    # 3️⃣ 수업 가능한 학생 수
    return n - len(lost)