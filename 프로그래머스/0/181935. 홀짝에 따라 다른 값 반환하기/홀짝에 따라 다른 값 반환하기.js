function solution(n) {
    var sum_odd = 0;
    var even = 0;
    if(n % 2 !== 0){
        for(let i = 1; i <= n; i += 2){
            sum_odd += i;
        }
        return sum_odd;
    }else{
        for(let i = 2; i <= n; i += 2){
            even += i * i;
        }
        return even;
    }
}