function solution(s) {
    var string = s.toUpperCase().split("");
    var count_p = 0;
    var count_y = 0;
    
    for (let c of string) {
        if (c === "P") count_p += 1;
        if (c === "Y") count_y += 1;
    }

    return count_p === count_y;
}
