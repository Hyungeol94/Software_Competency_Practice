//https://leetcode.com/problems/make-array-elements-equal-to-zero/?envType=daily-question&envId=2025-10-28
//3354. Make Array Elements Equal to Zero

/**
 * @param {number[]} nums
 * @return {number}
 */

var countValidSelection = function(buffer, i) { 
    var count = 0
    for (is_leftward of [true, false]) { 
        var pos = i
        var nums = [...buffer]
        while (0 <= pos && pos < nums.length) { 
            if (nums[pos] == 0) { 
                pos = pos + (is_leftward ? -1 : 1)
            } else { 
                nums[pos] -= 1 
                is_leftward = !is_leftward
                pos = pos + (is_leftward ? -1 : 1)
            }
        }
        if (nums.reduce((acc, curr) => (curr == 0 ? acc+1 : acc), 0) == nums.length) { 
            count += 1
        }
    }
    return count
}

var countValidSelections = function(nums) {
    var count = 0
    for (const [i, num] of nums.entries()) { 
        if (num === 0) { 
            count += countValidSelection(nums, i)
        }
    }
    return count
};