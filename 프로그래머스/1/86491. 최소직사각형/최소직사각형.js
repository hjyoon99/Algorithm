function solution(sizes) {
  //가로 세로 고정, 회전해서 가장 큰 값과 작은 값 고정.
    var rotated = sizes.map(([w, h]) => {
        return w > h ? [w, h] : [h, w];
    });
    
    // 가로 최대, 세로 최대
    var max_w = Math.max(...rotated.map(([w, _]) => w));
    var max_h = Math.max(...rotated.map(([_, h]) => h));
    
    return max_w * max_h;
}