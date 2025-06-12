function solution(sides) {
    var max = Math.max(...sides);
    var index = sides.indexOf(max);
    var arr = [...sides];
    arr.splice(index, 1);
    return max < arr.reduce((sum, curr) => sum + curr, 0) ? 1 : 2;
}