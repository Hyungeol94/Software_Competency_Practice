//https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/?envType=daily-question&envId=2026-07-27
//1464. Maximum Product of Two Elements in an Array

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums){
    nums.sort((a,b) => {
        return a-b
    })
    n = nums.length 
    return parseInt(BigInt(nums[n-1]-1) *BigInt(nums[n-2]-1))
    
};