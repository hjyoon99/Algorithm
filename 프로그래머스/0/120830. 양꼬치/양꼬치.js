function solution(n, k) {
    drink = k;
    if (n >= 10){
        drink = k - (Math.floor(n / 10));
    }
    return 12000 * n + 2000 * drink;
}