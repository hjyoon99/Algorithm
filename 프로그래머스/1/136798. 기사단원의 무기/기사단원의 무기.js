function solution(number, limit, power) {
    var answer = [];
    for(let j = 1; j <= number; j++){
        var pow = 0;
        for(i = 1; i * i <= j; i++){
            if (j % i === 0) {
                pow += (i*i === j) ? 1 : 2;
            }
        }
        if (pow > limit) pow = power;
        answer.push(pow);
    }
    
    return answer.reduce((sum, curr) => sum + curr, 0);
}