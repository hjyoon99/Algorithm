function solution(numbers) {
    var max1 = Math.max(...numbers);
    var index = numbers.indexOf(max1);
    numbers.splice(index, 1);
    var max2 = Math.max(...numbers);
    return max1 * max2;
}