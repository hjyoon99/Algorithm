function solution(x, n) {
    var answer = [];
    let a = x;
    for(let i = 0; i < n ; i++){
        answer.push(a);
        a += x;
    }
    return answer;
}