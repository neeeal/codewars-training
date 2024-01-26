function expandedForm(num) {
  const str_num = num.toString()
  let result = ''
  for(let i=0; i<str_num.length; i++){
    console.log(str_num[i])
    if(i==0){
      result = str_num[i]
    } else if(str_num[i]=='0'){
      result = result + '0'
    } else{
      result = result + ' + '
    }
    console.log(result)
  }
  return result
}
  module.exports = expandedForm