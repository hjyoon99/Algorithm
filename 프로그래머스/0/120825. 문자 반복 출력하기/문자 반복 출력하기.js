function solution(my_string, n) {
    var str = my_string.split("");
    for(let i = 0; i < str.length; i++){
        str.splice(i, 1, str[i].repeat(n));
    }
    return str.join("");
}