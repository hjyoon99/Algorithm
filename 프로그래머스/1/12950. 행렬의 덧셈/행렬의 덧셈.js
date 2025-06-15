function solution(arr1, arr2) {
    return arr1.map((val, idx) => 
                    val.map((val2, idx2) => 
                    val2 + arr2[idx][idx2]));
}