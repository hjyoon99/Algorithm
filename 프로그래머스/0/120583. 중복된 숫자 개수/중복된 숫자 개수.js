function solution(array, n) {
    return array.reduce((sum, curr) => {
        return curr === n ? sum + 1 : sum
    }, 0);
}