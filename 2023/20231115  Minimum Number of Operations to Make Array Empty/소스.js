// 2870. Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
  nums_set = new Set(nums)
  console.log(nums_set)
  let nums_dict = {}
  for (const item of nums_set){
      nums_dict[item] = 0
  }
  for (const num of nums) {
      nums_dict[num] += 1
  }
  console.log(nums_dict)
  let count = 0
  for (const key in nums_dict){
      if ((nums_dict[key] % 3) == 0){
          count += (nums_dict[key] / 3)
          continue
      }
      else if ((nums_dict[key] > 2)  && (nums_dict[key]-2)%3==0){
          count += ((nums_dict[key]-2) / 3)
          count += 1
          continue
      }
      else if ((nums_dict[key] > 4) && (nums_dict[key]-4)%3==0){
          count += ((nums_dict[key]-4) / 3)
          count += 2
          continue
      } 
      else if ((nums_dict[key] % 2) == 0){
          count += (nums_dict[key] / 2)
          continue
      }
      return -1
  }
  return count 
};