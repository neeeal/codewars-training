function order(words){
  const arrangement = words.split(" ").map((i)=>Number(i.replace(/\D/g, "")-1));
  const wordsList = words.split(" ");
  const result = []
  for (let i=0; i<arrangement.length; i++){
    result.push(wordsList[arrangement.indexOf(i)])
  }
  return result.join(" ")
}
  module.exports = order