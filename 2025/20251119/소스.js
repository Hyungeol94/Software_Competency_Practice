//https://leetcode.com/problems/keep-multiplying-found-values-by-two/?envType=daily-question&envId=2025-11-19
//2154. Keep Multiplying Found Values by Two

/**
 * @param {number[]} nums
 * @param {number} original
 * @return {number}
 */
var findFinalValue = function(nums, original) {
    while (true) { 
        if (!nums.find((item) => item == original)) { 
            break
        }
        original *= 2
    }
    return original
};