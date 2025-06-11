function solution(quiz) {
    return quiz.map(q=>{
        const [x, op, y, , z] = q.split(" ");
        const result = op === '+' ? Number(x) + Number(y) : Number(x) - Number(y);
        return result === Number(z) ? "O" : "X";
    });
}