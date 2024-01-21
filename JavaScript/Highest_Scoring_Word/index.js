function high(x){
  const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('')
  const words = x.split(' ')
  const values = words.map((word)=>
                        word.split('').map((value)=> 
                            alphabet.indexOf(value)+1).reduce((acc,value)=>acc+value))
  const result = words[values.indexOf(Math.max(...values))]
  return result
}
  module.exports = high