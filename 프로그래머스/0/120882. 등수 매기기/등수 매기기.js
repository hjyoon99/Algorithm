function solution(score) {
    var answer = [];
    for(let i = 0; i < score.length; i++){
        const avg = score[i].reduce((acc, curr) => acc + curr, 0) / score[i].length;
        answer.push(avg);
    }
    const sorted = [...answer].sort((a, b) => b-a);
    const ranks = answer.map(score => sorted.indexOf(score) + 1);
    return ranks;
}