//2869. Minimum Operations to Collect Elements
//https://leetcode.com/problems/minimum-operations-to-collect-elements/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
function isFalse(item){
  if (item === false){
      return true
  }
  else
      return false
}

var minOperations = function(nums, k) {
  const visited = []
  for(let i = 0;i<=k;i++){
      visited.push(false)
  }
  visited[0] = true

  let count = 0
  while (visited.length!=0){
      const lastElement = nums.pop()        
      console.log(lastElement)
      count += 1
      visited[lastElement] = true
      if (visited.find(isFalse)!==undefined)
          continue;
      return count
  }

};