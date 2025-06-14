function gdc(a, b){
    while(b !== 0){
        const tmp = b;
        b = a % b;
        a = tmp;
    }
    return a;
}

function lcm(a, b){
    return (a*b) / gdc(a, b);
}
function solution(n, m) {
    return [gdc(n, m), lcm(n, m)];
    
}