function solution(N, stages) {
    let answer = [];
    let fails = [];
    stages.sort((a, b) => b - a);
    //console.log(stages);
    
    for(let i = 1; i <= N; i++){
        let clear = 0;
        let no_clear = 0;
        let fail = 0;
        for(let person of stages){
            // stage 도달 : i 보다 큰 값
            if(person > i) clear += 1;
            // 도달했으나 클리어 못한 : i 
            if(person === i) no_clear += 1;
        }
        fail = no_clear / (clear + no_clear);
        fails.push([i, fail])
    }
    fails.sort((a, b) => b[1] - a[1]);
    console.log(fails);
    return fails.map((x) => x[0]);
    
}