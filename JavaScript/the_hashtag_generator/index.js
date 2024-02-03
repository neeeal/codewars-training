function generateHashtag (str) {
  const strConnected = str.trim().replace(/ /g,"<WHTSPC>") || false
  if (!strConnected) return false
  const result = "#" + strConnected.split("<WHTSPC>").map((word)=>word!==""?word[0].toUpperCase()+word.slice(1,word.length):null).join("")
  if(result.length > 140) return false
  return result
}
  module.exports = generateHashtag