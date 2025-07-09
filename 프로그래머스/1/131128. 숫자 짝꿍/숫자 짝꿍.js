function solution(X, Y) {
    const xCount = Array(10).fill(0);
    const yCount = Array(10).fill(0);

    // 각 숫자 빈도 세기
    for (let ch of X) xCount[Number(ch)]++;
    for (let ch of Y) yCount[Number(ch)]++;

    let result = '';

    // 9부터 0까지 돌면서 가능한 조합 추출 (큰 수부터)
    for (let i = 9; i >= 0; i--) {
        const count = Math.min(xCount[i], yCount[i]);
        result += i.toString().repeat(count);
    }

    if (result === '') return '-1';
    if (result[0] === '0') return '0';  // '000' 같은 경우

    return result;
}
