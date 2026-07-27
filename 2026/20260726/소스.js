//https://leetcode.com/problems/maximum-product-of-three-numbers/submissions/2082619283/?envType=daily-question&envId=2026-07-26
//628. Maximum Product of Three Numbers

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumProduct = function(nums) {
    nums.sort((a, b) => {
        if (a < b) {
        return -1
        } else if ( a > b) {
        return 1
        } else{
        return 0
        }
    })
    
    const leftProduct = nums.slice(0, 3).reduce((acc, val )=> acc*val)
    const rightProduct = nums.slice(nums.length-3).reduce((acc, val) => acc*val)
    const combiProduct = nums.slice(0, 2).reduce((acc, val) => acc*val) * nums[nums.length-1]
    return Math.max(leftProduct,  rightProduct, combiProduct)
}