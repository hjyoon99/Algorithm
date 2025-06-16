function solution(a, b, n) {
    var count = 0;
    while(n >= a){
        var ret = (Math.floor(n / a)) * b;
        count += ret;
        n = n - (a * Math.floor(n / a)) + ret;
        console.log(n);
    }
    return count;
}