function countDiv(n){
    var count = 0;
    for(let i = 1; i <= n; i++){
        if(n % i === 0){
            if(i * i === n){
                count += 1;
            }else count += 2;
        }
    }
    return count;
}
function solution(left, right) {
    var answer = 0;
    for(let i = left; i <= right; i++){
        if(countDiv(i) % 2 === 0) answer += i;
        else answer -= i;
    }
    return answer;
}