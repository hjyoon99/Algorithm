function solution(arr)
{
    var answer = [];
    var tmp = arr[0];
    answer.push(arr[0]);
    for (let a of arr) {
        if (a !== tmp) {
            answer.push(a);
            tmp = a;
        }
    }
    return answer;
}