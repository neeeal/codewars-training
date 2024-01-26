function expandedForm(num) {
  const str_num = num.toString()
  let result = str_num[0].toString()+'0'.repeat(str_num.length-1)
  for(let i=1; i<str_num.length; i++){
    result = str_num[i]!=='0' ? result + ' + ' + str_num[i]+'0'.repeat(str_num.length-i-1) : result
  }
  return result
}
  module.exports = expandedForm