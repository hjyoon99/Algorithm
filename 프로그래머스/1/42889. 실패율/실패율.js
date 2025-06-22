function solution(N, stages) {
    var answer = [];
    let stageCount = Array(N+2).fill(0);
    
    for(let s of stages){
        stageCount[s] += 1;
    }
    
    let totalPlayer = stages.length;
    
    for(let i = 1; i <= N; i++){
        let fail = stageCount[i] / totalPlayer;
        answer.push([i, fail]);
        totalPlayer -= stageCount[i];
    }
    answer.sort((a, b) => b[1] - a[1]);
    
    return answer.map(a => a[0]);
}