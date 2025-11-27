//https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/?envType=daily-question&envId=2025-11-27
//3381. Maximum Subarray Sum With Length Divisible by K

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxSubarraySum = function(nums, k) {
    const minPrefixSum = new Map()
    let acc = 0
    let maxVal = -Infinity
    for (const [i, num] of nums.entries()) { 
        acc += num
        if (i >= k) { 
            maxVal = Math.max(maxVal, acc-(minPrefixSum.get(i%k) ?? Infinity))
        }
        minPrefixSum.set(i%k, Math.min(minPrefixSum.get(i%k) ?? Infinity, acc))
        if ((i+1) % k === 0) { 
            maxVal = Math.max(maxVal, acc)
        }
    }
    return maxVal
};