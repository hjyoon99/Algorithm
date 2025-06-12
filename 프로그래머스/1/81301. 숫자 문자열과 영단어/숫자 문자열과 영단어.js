function solution(s) {
    const alpha = {
        zero : 0,
        one : 1,
        two : 2,
        three : 3,
        four : 4,
        five : 5,
        six : 6,
        seven : 7,
        eight : 8,
        nine : 9
    }
    
    for(const word in alpha){
        s = s.replace(new RegExp(word, 'g'), alpha[word]);
    }
    return Number(s);
    
    
}