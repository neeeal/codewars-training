function rgb(r, g, b) {
    const HEX = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    return [r,g,b].reduce((acc,curr)=>{
        return curr < 0 ? acc + '00'
        : curr > 255 ? acc + 'FF'
        :acc + `${HEX[Math.floor(curr/16)%16]}` + `${HEX[curr%16]}`      
        }
    , ''
    )
}
  module.exports = rgb