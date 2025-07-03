function solution(s) {
    let idx = 0;
    let str = s.split("");
    let answer = 0;
    
    while(idx < str.length){
        let x = str[idx];
        let countx = 0;
        let notx = 0;
    for(let i=idx; i < str.length; i++){
        if(str[i] === x) countx += 1;
        else notx += 1;
        
        if(countx === notx) {
            answer += 1;
            idx = i+1;
            break;
        }
        
        // 문자열 끝까지 갔는데도 countx !== notx인 경우
        if (i === str.length -1){
            answer += 1;
            idx = str.length;
        }

    }
}
    return answer;
}