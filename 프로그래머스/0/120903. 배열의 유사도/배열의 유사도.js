function solution(s1, s2) {
    var answer = 0;
    for (const c of s1){
        if (s2.includes(c)){
            answer += 1;
        }
    }
    return answer;
}