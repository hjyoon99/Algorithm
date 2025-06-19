function solution(n) {
    const divisorCount = Array(n + 1).fill(0);

    // 1부터 n까지 모든 수의 약수 개수 누적
    for (let i = 1; i <= n; i++) {
        for (let j = i; j <= n; j += i) {
            divisorCount[j] += 1;
        }
    }

    // 예시: 약수의 개수가 2인 수(소수)의 개수 세기
    let answer = 0;
    for (let i = 2; i <= n; i++) {
        if (divisorCount[i] === 2) answer += 1;
    }

    return answer;
}