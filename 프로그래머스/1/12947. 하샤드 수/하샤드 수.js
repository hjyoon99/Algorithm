function solution(x) {
    var sum = String(x).split("").reduce((sum, curr) => sum + Number(curr), 0);
    return (x % sum === 0);
}