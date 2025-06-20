function solution(nums) {
    function isPrime(n) {
        if (n < 2) return false;
        for (let i = 2; i <= Math.sqrt(n); i++) {
            if (n % i === 0) return false;
        }
        return true;
    }

    function getComb(arr, r){
        const result = [];

        const combine = (path, start) => {
            if (path.length === r){
                const sum = path.reduce((sum, curr) => sum + curr, 0);
                result.push(sum);
                return;
            }
            for (let i = start; i < arr.length; i++){
                path.push(arr[i]);
                combine(path, i+1);
                path.pop();
            }
        };

        combine([], 0);
        return result;
    }

    let answer = 0;
    const sums = getComb(nums, 3); // 3개를 더한 모든 조합

    for (let s of sums) {
        if (isPrime(s)) {
            answer += 1;
        }
    }

    return answer;
}