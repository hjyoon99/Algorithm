function solution(num_list) {
    var nums = num_list.filter(x => x % 2 === 0);
    var nums2 = num_list.filter(x => x % 2 !== 0);
    var answer = [];
    answer.push(nums.length);
    answer.push(nums2.length);
    return answer;
}