function cipher(ch, shift){
    let code = ch.charCodeAt(ch);
    if(code >= 65 && code <= 90){
        return String.fromCharCode((code - 65 + shift) % 26 + 65);
    }
    if(code >= 97 && code <= 122){
        return String.fromCharCode((code - 97 + shift) % 26 + 97);
    }
    return ch;
}
function solution(s, n) {
    var string = s.split("");
    var answer = "";
    for(let str of string){
        answer += cipher(str, n);
    }
    return answer;
}