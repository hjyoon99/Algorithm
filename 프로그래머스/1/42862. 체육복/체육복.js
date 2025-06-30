function solution(n, lost, reserve) {
    
    // 정렬은 필수!
  lost.sort((a, b) => a - b);
  reserve.sort((a, b) => a - b);
  let realLost = lost.filter(x => !reserve.includes(x));
  let realReserve = reserve.filter(x => !lost.includes(x));

  for (let r of realReserve) {
    if (realLost.includes(r - 1)) {
      realLost = realLost.filter(x => x !== r - 1);
    } else if (realLost.includes(r + 1)) {
      realLost = realLost.filter(x => x !== r + 1);
    }
  }

  return n - realLost.length;
}
