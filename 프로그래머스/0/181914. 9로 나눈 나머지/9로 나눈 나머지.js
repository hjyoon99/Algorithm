function solution(number) {
    let n = number.split('').reduce((sum , curr) => Number(curr) + sum, 0);
    return n % 9;
}