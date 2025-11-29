//https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/?envType=daily-question&envId=2025-11-29
//3512. Minimum Operations to Make Array Sum Divisible by K

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    return nums.reduce((acc, curr) => (acc+curr), 0) % k
};
