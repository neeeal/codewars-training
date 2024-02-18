function operation(arr) {
    const val = arr.split(" ")
    const first = Number(val[0])
    const strOp = val[1]
    const sec = Number(val[2])
    const result = strOp === '+' ? first + sec
                  :strOp === '-' ? first - sec
                  :strOp === '*' ? first * sec
                  :Math.floor(first/sec)
    return result
  }
  
  function zero(str = null) {
    const number = '0' 
    return str ? operation(number + str) : number
  }
  function one(str = null) {
    const number = '1' 
    return str ? operation(number + str) : number
  }
  function two(str = null) {
    const number = '2' 
    return str ? operation(number + str) : number
  }
  function three(str = null) {
    const number = '3' 
    return str ? operation(number + str) : number
  }
  function four(str = null) {
    const number = '4' 
    return str ? operation(number + str) : number
  }
  function five(str = null) {
    const number = '5' 
    return str ? operation(number + str) : number
  }
  function six(str = null) {
    const number = '6' 
    return str ? operation(number + str) : number
  }
  function seven(str = null) {
    const number = '7' 
    return str ? operation(number + str) : number
  }
  function eight(str = null) {
    const number = '8' 
    return str ? operation(number + str) : number
  }
  function nine(str = null) {
    const number = '9' 
    return str ? operation(number + str) : number
  }
  
  function plus(number) {
    return ` + ${number}`
  }
  function minus(number) {
    return ` - ${number}`
  }
  function times(number) {
    return ` * ${number}`
  }
  function dividedBy(number) {
    return ` / ${number}`
  }
module.exports = [zero, one, two, three, four, five, six, seven, eight, nine, plus, minus, times, dividedBy]