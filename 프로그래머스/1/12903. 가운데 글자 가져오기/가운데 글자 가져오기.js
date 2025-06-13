function solution(s) {
    var target = Math.floor(s.length / 2);
    if (s.length % 2 === 0){
        return s.slice(target - 1, target + 1);
    }else return s[target];
}