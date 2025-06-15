function solution(numbers) {
    var ans = [];
    var idx = 0;
    while(idx < numbers.length - 1){
        for(let i = idx + 1; i < numbers.length; i++){
            ans.push(numbers[idx] + numbers[i]);
        }
        idx += 1;
    }
    ans.sort((a, b) => a - b);
    var answer = [...new Set(ans)]
    return answer;
}