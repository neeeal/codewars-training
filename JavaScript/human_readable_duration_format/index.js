function formatDuration (seconds) {
  if(seconds===0) return 'now';
  if(seconds<0) return;
  
  let result = '';
  try{
    const data = {
      years:0,
      days:0,
      hours:0,
      minutes:0,
      seconds:0
    }
    
    data.seconds = seconds%60;
    data.minutes = Math.floor(seconds/60)%60;
    data.hours = Math.floor(seconds/(60*60))%24;   
    data.days = Math.floor(seconds/(60*60*24))%365;   
    data.years = Math.floor(seconds/(60*60*24*365)) ;
    
    let keys = [];
    Object.keys(data).forEach(key=>{
      if(data[key]===0) delete data[key];
      else keys.push(key);
    })
    
    let length = keys.length;
    
    if(length>2){
      for(let i=0; i<length-2; i++){
        result = data[keys[i]] === 1 
          ? result + `${data[keys[i]]} ${keys[i].slice(0,keys[i].length-1)}, ` 
        : result + `${data[keys[i]]} ${keys[i]}, `;
      }
      keys = keys.slice(length-2) 
      length = keys.length
    }
    
    if(length===2){
      const and = ' and '
      result = data[keys[0]] === 1 
        ? result + `${data[keys[0]]} ${keys[0].slice(0,keys[0].length-1)}` 
      : result + `${data[keys[0]]} ${keys[0]}`;
      result = data[keys[1]] === 1 
        ? result + and + `${data[keys[1]]} ${keys[1].slice(0,keys[1].length-1)}` 
      : result + and + `${data[keys[1]]} ${keys[1]}`;
    }
    
    if(length===1)
      result = data[keys[0]] === 1 
        ? `${data[keys[0]]} ${keys[0].slice(0,keys[0].length-1)}` 
      : `${data[keys[0]]} ${keys[0]}`;
    
    return result.trim()
    
  }catch(error){
    console.log(error)
    return error
  }
}
  module.exports = formatDuration