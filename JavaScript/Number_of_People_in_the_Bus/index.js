var number = function(busStops){
  return busStops.map((x)=> x[0]-x[1]).reduce((acc, value)=> acc+value)
}
  module.exports = number