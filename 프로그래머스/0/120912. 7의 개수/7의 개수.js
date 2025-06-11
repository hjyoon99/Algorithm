function solution(array) {
    const cnt = array.reduce((sum, num) => {
        const numInArr = num.toString().split("").filter(char => char === '7').length;
        return sum + numInArr;
        },0)
    return cnt;
}