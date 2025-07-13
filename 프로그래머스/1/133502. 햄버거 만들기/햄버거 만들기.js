function solution(ingredient) {
    let answer = 0;
    const target = [1, 2, 3, 1];
    let i = 0;

    while (i <= ingredient.length - 4) {
        const sliced = ingredient.slice(i, i + 4);
        if (sliced.join('') === target.join('')) {
            ingredient.splice(i, 4); 
            answer++;
            i = i - 3;  
        } else {
            i++;
        }
    }

    return answer;
}