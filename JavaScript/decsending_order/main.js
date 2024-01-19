function descendingOrder(n){
    const str_n = n.toString()
    const set_n = new Set(str_n.split('').sort((a,b)=>b-a))
    const set_n_values = set_n.values()
    let result = ''
    for (let i=0; i<set_n.size; i++){
      count = 0
      let x = set_n_values.next().value
      for (let j=0; j<str_n.length; j++){
      result += str_n[j]==x ? str_n[j] : ''
      }
    }
    return parseInt(result)
  }
  module.exports = descendingOrder