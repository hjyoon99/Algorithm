function solution(num_list) {
    return num_list.length >= 11 ? num_list.reduce((sum, curr) => sum + curr) : num_list.reduce((sum, curr) => sum * curr);
}