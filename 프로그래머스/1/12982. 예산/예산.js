function solution(d, budget) {
    d.sort((a, b) => a - b);
    var count = 0;
    var ok = 0;
    for(let money of d){
        ok += money;
        if(ok <= budget){
            count += 1;
        }else break;
    }
    return count;
}