function solution(array, commands) {
    var answer = []
    for(let c of commands){
        const [i, j, k] = c;
        var arr = array.slice(i-1, j);
        arr.sort((a, b) => a - b);
        answer.push(arr[k-1])
    }
    return answer;
}