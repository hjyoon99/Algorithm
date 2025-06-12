function solution(num_list) {
    if (num_list.length >= 11){
        return num_list.reduce((sum, curr) => sum + curr);
    }else{
        return num_list.reduce((sum, curr) => sum * curr);
    }
}