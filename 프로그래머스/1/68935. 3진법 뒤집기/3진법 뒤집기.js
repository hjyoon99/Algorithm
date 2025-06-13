function solution(n) {
    var reverse_thr = n.toString(3).split("").reverse().join("");
    return parseInt(reverse_thr, 3);
}