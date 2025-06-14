function solution(s) {
    return s.split(/(\s)/)  // 공백도 배열에 포함
        .map(word => {
            if (word === " ") return word;  // 공백은 그대로
            return [...word]
                .map((ch, idx) => idx % 2 === 0 ? ch.toUpperCase() : ch.toLowerCase())
                .join('');
        }).join('');
}