function solution(a, b) {
    var weeks = ["THU", "FRI" ,"SAT", "SUN", "MON", "TUE", "WED", "THU"];
    var days = 0;
    if (a === 1){
        return weeks[b % 7];
    }
    a -= 1
    while(a > 0){
        if (a === 2){
            days +=  29;
        }else if (a === 1 || a === 3 || a === 5 || a === 7 || a === 8 || a === 10 || a === 12) {
            days +=  31;
        }else days +=  30;
        console.log(a, days);
        a -= 1;
    }
    days += b;
    
    return weeks[days % 7];
    
}