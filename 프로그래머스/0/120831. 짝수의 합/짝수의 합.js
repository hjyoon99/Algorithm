function solution(n) {
    var answer = [];
    for (let i = 2; i <= n; i += 2){
        answer.push(i);
    }
    return answer.reduce((sum, curr) => sum + curr, 0);
    
}