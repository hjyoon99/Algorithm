function solution(polynomial) {
    var terms = polynomial.split(" + ");
    var numSum = 0;
    var xSum = 0;
    
    for (let term of terms){
        if (term === '+') continue;
    
        if (term.includes('x')){
            let c = term.replace('x', '');
            xSum += c === '' ? 1 : Number(c);
        }else{
            numSum += Number(term);
        }
    }
    
    let answer = [];
    
    if(xSum !== 0){
        answer.push(xSum === 1 ? 'x' : `${xSum}x`);
    }
    
    if(numSum !== 0){
        answer.push(numSum);
    }
    return answer.join(" + ");
}