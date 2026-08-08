//https://leetcode.com/problems/find-missing-elements/description/?envType=daily-question&envId=2026-08-04
//3731. Find Missing Elements

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findMissingElements = function(nums) {
    const maxVal = nums.reduce((acc, num) => Math.max(acc, num))
    const minVal = nums.reduce((acc, num) => Math.min(acc, num))
    nums.sort((a, b) => {
return a - b
    })
    
    const allArray = []
    for (let i = minVal; i < maxVal; i++){
        allArray.push(i)
    }
    const n = nums.length
    const res = []
    let j = 0
    for (let i = 0; i < n; i++){
        while (allArray[j] < nums[i]) {
            res.push(allArray[j])
            j += 1
        }
        j += 1
    }
    return res
};
