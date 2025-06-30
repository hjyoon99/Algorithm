function solution(nums) {
    let maxP = new Set(nums).size;
    let pick = nums.length / 2;
    
    return Math.min(maxP, pick);
}