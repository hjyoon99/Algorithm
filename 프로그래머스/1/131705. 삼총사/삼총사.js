function solution(number) {
    var answer = 0;
    var idx = 0;
    while(idx < number.length-1){
        for(let i = idx + 1; i < number.length; i++){
            for(let j = i + 1; j < number.length; j++){
                if((number[idx] + number[i] + number[j]) === 0) answer += 1;
            }
        }
        idx += 1;
    }
    return answer;
}