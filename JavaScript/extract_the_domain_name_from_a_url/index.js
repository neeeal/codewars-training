function domainName(url){
  result = url.includes('www') ? url.split('.')[1] 
            : url.includes('http') ? url.split('//')[1].split('.')[0]
            : url.split('.')[0]
  return result
}
  module.exports = domainName