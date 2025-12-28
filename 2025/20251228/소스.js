//https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/?envType=daily-question&envId=2025-12-28
//1351. Count Negative Numbers in a Sorted Matrix

/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function(grid) {
    return grid.map((row) => { 
        //return the count of negative numbers
        return row.filter((a) => a < 0).length
    }).reduce((a, b) => a+b)
};