function cakes(recipe, available) {
  let quantity = 0
  let flag = true
  while (true){
    for (let key in recipe){
      flag = available.hasOwnProperty(key) ? true : false
      available[key] = available[key] - recipe[key]
      flag = available[key] >= 0 ? true : false
      if (flag === false) return quantity
    } 
    quantity++
  }
}
  module.exports = cakes