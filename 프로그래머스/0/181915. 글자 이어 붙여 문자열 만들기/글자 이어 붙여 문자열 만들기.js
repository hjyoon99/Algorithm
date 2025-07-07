function solution(my_string, index_list) {
    let str = my_string.split("");
    let answer = '';
    for(let idx of index_list){
        answer += str[idx];
    }
    return answer;
}