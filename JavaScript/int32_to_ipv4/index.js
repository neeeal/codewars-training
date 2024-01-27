function int32ToIp(int32){
  let rem = []
  for(let i=0; i<4; i++){
    rem.unshift(int32%256)
    int32 = Math.floor(int32/256)
  }
  return rem.join(".")
}
  module.exports = int32ToIp