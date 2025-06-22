function solution(babbling) {
    const valid = ["aya", "ye", "woo", "ma"]; 
    let answer = 0;

    for (let word of babbling) {
        let temp = word;        
        let last = "";          
        let isValid = true;     

        while (temp.length > 0) {
            let found = false;  

            for (let v of valid) {
                if (temp.startsWith(v) && last !== v) {
                    temp = temp.slice(v.length); 
                    last = v;                    
                    found = true;
                    break;                       
                }
            }

            if (!found) {
                isValid = false;
                break;
            }
        }

        if (isValid) answer++; 
    }

    return answer;
}
