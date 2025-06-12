function solution(num) {
    var i = 1;
    var n = num;
    var cnt = 0;
    while (i <= 500){
        if (num === 1) return 0;
        if (n % 2 === 0) {
            n /= 2;
        }else n = (n * 3) + 1;
        if (n === 1) return i;
        i++;
    }
    return -1;
}