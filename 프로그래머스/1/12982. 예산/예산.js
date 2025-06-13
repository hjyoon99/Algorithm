function solution(d, budget) {
    return d.sort((a, b) => a - b).reduce((count, money) => {
        return count + ((budget -= money) >= 0);
    }, 0)
}