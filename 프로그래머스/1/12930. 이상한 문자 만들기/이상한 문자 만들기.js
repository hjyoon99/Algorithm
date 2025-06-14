function solution(s) {
    var chunk = s.split(" ");
    var sol = '';
    for(let c of chunk){
        var answer = '';
        for(let i = 0; i < c.length; i++){
            if (i % 2 === 0){
                var tmp = c[i].toUpperCase();
                answer += tmp;
            }else answer += c[i].toLowerCase();
        }
        sol += answer + " ";
    }
    return sol.slice(0, sol.length-1);
}
