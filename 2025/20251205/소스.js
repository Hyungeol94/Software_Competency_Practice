//https://leetcode.com/problems/count-partitions-with-even-sum-difference/?envType=daily-question&envId=2025-12-05
//3432. Count Partitions with Even Sum Difference

/**
 * @param {number[]} nums
 * @return {number}
 */
var countPartitions = function(nums) {
    const prefixSum = []
    const postfixSum = []
    let acc = 0
    for (num of nums) {
        acc += num
        prefixSum.push(acc)
    }

    for (const [i, num] of nums.entries()) { 
        postfixSum.push(acc-prefixSum[i])
    }
    
    let count = 0
    for (let i = 0; i < nums.length-1 ; i++) { 
        const diff = Math.abs(prefixSum[i]-postfixSum[i])
        if ( diff % 2 == 0) { 
            count += 1 
        }
    }
    
    return count
    
};