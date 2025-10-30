//https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/?envType=daily-question&envId=2025-10-30
//1526. Minimum Number of Increments on Subarrays to Form a Target Array

/**
 * @param {number[]} target
 * @return {number}
 */

var minNumberOperations = function(target) {
    if (target.length == 1) { 
        return target[0]
    }

    const nums = target
    const n = nums.length
    var numOperations = 0
    var left = 0
    var right = 1
    var peakVal = nums[left]
    var minVal = 0

    while (right < n) { 
        if (nums[left] > nums[right]) { 
            numOperations += (peakVal - minVal)
            minVal = nums[right]
            peakVal = nums[right]
        } else { 
            minVal = Math.min(minVal, nums[left])
            peakVal = Math. max(peakVal, nums[right])
        }
        left += 1
        right += 1
    }

    left -= 1
    right -= 1
    if (nums[left] <= nums[right]) { 
        numOperations += (peakVal - minVal)
    }
    
    return numOperations
};