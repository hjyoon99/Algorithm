function solution(s) {
    var Upper = "";
    var Lower = "";
    for (let a of s){
           if (a === a.toLowerCase()){
                Lower += a;
           }else Upper += a;
       }
    Lower = Lower.split("").sort().reverse().join("");
    Upper = Upper.split("").sort().reverse().join("");
    return Lower + Upper;
}