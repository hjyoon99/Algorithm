function solution(n)
{
    var answer = String(n).split("");
    return answer.reduce((sum, curr) => sum + Number(curr), 0);
}