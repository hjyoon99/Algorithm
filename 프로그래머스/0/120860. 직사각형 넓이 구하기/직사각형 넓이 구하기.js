function solution(dots) {
    var x = dots.map(d => d[0]);
    var y = dots.map(d => d[1]);
    
    var sqrX = Math.max(...x) - Math.min(...x);
    var sqrY = Math.max(...y) - Math.min(...y);
    
    return sqrX * sqrY;
}