function solution(dartResult) {
    let rounds = dartResult.match(/\d{1,2}[SDT][*#]?/g);
    let scores = [];
    
    for(let i = 0; i < rounds.length; i++){
        const round = rounds[i];
    
        const score = parseInt(round.match(/\d{1,2}/)[0]); // 숫자
        const bonus = round.match(/[SDT]/)[0];            // 보너스
        const option = round.match(/[*#]/)?.[0];           // 옵션 (*, # 또는 없음)
        
        // 보너스 처리
        let calculated = Math.pow(score, { S:1, D:2, T:3 }[bonus]);
        
        // 옵션 처리
        if (option === "*"){
            calculated *= 2;
            if (i > 0) scores[i-1] *= 2;
        }else if (option === "#"){
            calculated *= (-1);
        }
        
        scores.push(calculated);
    }
    return scores.reduce((sum, curr) => sum + curr, 0);
}