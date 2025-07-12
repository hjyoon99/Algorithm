function solution(ingredient) {
    let answer = 0;
    const target = [1, 2, 3, 1];
    let i = 0;

    while (i <= ingredient.length - 4) {
        const sliced = ingredient.slice(i, i + 4);
        if (JSON.stringify(sliced) === JSON.stringify(target)) {
            ingredient.splice(i, 4);  // 제거
            answer++;
            i = Math.max(i - 3, 0);  // 이전으로 백트래킹
        } else {
            i++;
        }
    }

    return answer;
}