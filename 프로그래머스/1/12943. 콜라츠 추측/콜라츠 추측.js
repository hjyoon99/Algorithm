function solution(num) {
    var i = 1;
    var cnt = 0;
    while (i <= 500){
        if (num === 1) return 0;
        if (num % 2 === 0) {
            num /= 2;
        }else num = (num * 3) + 1;
        if (num === 1) return i;
        i++;
    }
    return -1;
}