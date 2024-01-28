function wave(str){
  const result = []
  let temp = ''
  let flag = true
  
  for(let i=0; i<str.length; i++){
    temp = str.split("")
    flag = temp[i]!==" " ? true : false
    if(!flag) continue
    temp[i] = temp[i].toUpperCase()
    result.push(temp.join(""))
  }
  
  return result
}
  module.exports = wave