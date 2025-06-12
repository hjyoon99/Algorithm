function solution(n) {
    var answer = String(n).split("");
    var sol = answer.reduce((sum, curr) => sum + Number(curr), 0);
    return sol;
}