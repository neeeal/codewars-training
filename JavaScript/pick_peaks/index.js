function pickPeaks(arr){
  const result = {pos:[], peaks:[]}
  const store = {pos:[], peaks:[]}
  let flag = true
  for(let i = 1; i < arr.length-1; i = i+1){
    let prev = arr[i-1]
    let curr = arr[i]
    let next = arr[i+1]
    if( prev < curr && curr > next){
      result.pos.push(i)
      result.peaks.push(curr)
      flag = true
    }
    if( prev<curr && curr===next && flag){
      flag = !flag
      store.pos.push(i)
      store.peaks.push(curr)
    }else if (store.peaks.length>0 && store.peaks[store.peaks.length-1] < next && !flag){
      flag = !flag
      store.pos.pop()
      store.peaks.pop()
    }else if(store.peaks[store.peaks.length-1] !== undefined && store.peaks[store.peaks.length-1] > next && !flag){
      result.pos.push(store.pos[store.pos.length-1])
      result.peaks.push(store.peaks[store.peaks.length-1])
      flag = !flag
    }
  } 
  return result
}
  module.exports = pickPeaks