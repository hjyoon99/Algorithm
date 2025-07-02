function solution(arr) {
    let sum = arr.reduce((curr, sum) => sum + curr, 0);
    return sum / arr.length;
}