function solution(array, height) {
    array.sort((a, b) => b-a);
    var sum = 0;
    for (let i = 0; i < array.length; i++){
        if(array[i] > height){
            sum += 1
        }else break;
    }
    return sum;
}