//https://leetcode.com/problems/smallest-number-with-all-set-bits/?envType=daily-question&envId=2025-10-29
//3370. Smallest Number With All Set Bits

/**
 * @param {number} n
 * @return {number}
 */
var smallestNumber = function(n) {
    var i = n
    while (true) { 
        num = i.toString(2)
        if (num.includes('0')) { 
            i += 1
            continue
        }
        return i
    }
};