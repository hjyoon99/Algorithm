function solution(n) {
    var answer = 0;
    for(let i=0; i <= Math.sqrt(n); i++){
        if(n % i === 0){
            answer += (i === n/i) ? 1 : 2;
        }
    }
    return answer;
}