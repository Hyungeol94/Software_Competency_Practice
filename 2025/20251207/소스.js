//https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/?envType=daily-question&envId=2025-12-07
//1523. Count Odd Numbers in an Interval Range

/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
    if ((high - low + 1) % 2 == 0) { 
        return Math.floor((high - low + 1) / 2)
    } else { 
        return low % 2 == 1 ? Math.floor((high - low + 1) / 2) + 1 : Math.floor((high - low + 1) / 2)
    }
};