function solution(array, height) {
    var answer = array.filter(arr => arr > height);
    return answer.length;
}