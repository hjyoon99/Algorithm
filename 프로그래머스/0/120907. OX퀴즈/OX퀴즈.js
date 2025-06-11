function solution(quiz) {
    return quiz.map(q=>{
        const [left, right] = q.split(" = ");
        const result = eval(left);
        return result === Number(right) ? "O" : "X";
    });
}