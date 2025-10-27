//https://leetcode.com/problems/number-of-laser-beams-in-a-bank/?envType=daily-question&envId=2025-10-27
//2125. Number of Laser Beams in a Bank

/**
 * @param {string[]} bank
 * @return {number}
 */
var numberOfBeams = function(bank) {
    var prevCount = 0
    var num = 0
    for (const [i, row] of bank.entries()) { 
        if (row.includes("1")) {
            var currCount = row.split("1").length-1
            num += prevCount * currCount
            prevCount = currCount
        }
    }
    return num
};