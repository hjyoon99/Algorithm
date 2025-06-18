function solution(answers) {
    var answer = [];
    var num_1 = [1,2,3,4,5];
    var num_2 = [2,1,2,3,2,4,2,5];
    var num_3 = [3,3,1,1,2,2,4,4,5,5];
    var count_1 = 0;
    var count_2 = 0;
    var count_3 = 0;
     for(let i = 0; i < answers.length; i++){
        if(answers[i] === num_1[i % 5]) count_1 += 1;
        if(answers[i] === num_2[i % 8]) count_2 += 1;
        if(answers[i] === num_3[i % 10]) count_3 += 1;
    }
    const maxScore = Math.max(count_1, count_2, count_3);

    if (count_1 === maxScore) answer.push(1);
    if (count_2 === maxScore) answer.push(2);
    if (count_3 === maxScore) answer.push(3);
    
    return answer;
}