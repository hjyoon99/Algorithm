function solution(participant, completion) {
    let answer = "";
    let players = new Map();
    for(let part of participant){
        players.set(part, (players.get(part) || 0) + 1);
    }
    for(let comp of completion){
       players.set(comp, players.get(comp) - 1);
    }
    for(let [k, v] of players){
        if (v !== 0) {
            answer = k;
            break;
        }
    }

    return answer;
}