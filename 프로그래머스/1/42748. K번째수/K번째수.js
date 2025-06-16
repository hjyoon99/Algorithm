function solution(array, commands) {
    var answer = []
    for(let c of commands){
        var arr = array.slice(c[0]-1, c[1]);
        arr.sort((a, b) => a - b);
        answer.push(arr[c[2]-1])
    }
    return answer;
}