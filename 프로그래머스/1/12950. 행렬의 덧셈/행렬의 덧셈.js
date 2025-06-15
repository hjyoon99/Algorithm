function solution(arr1, arr2) {
    var answer = [];
    for(let j = 0; j < arr1.length; j++){
        var row = [];
        for(let i = 0; i < arr1[j].length; i++){
           row.push(arr1[j][i] + arr2[j][i]);
        }
        answer.push(row);
    }
    return answer;
}