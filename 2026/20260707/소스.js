//https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/submissions/2059134702/?envType=daily-question&envId=2026-07-07
//3754. Concatenate Non-Zero Digits and Multiply by Sum I

/**
 * @param {number} n
 * @return {number}
 */
var sumAndMultiply = function(n) {
    let sum = BigInt(0)
    let x = ""
    for (const [c] of String(n)) {
        sum += BigInt(parseInt(c))
        if (c != '0') {
            x = x+c
        }
    }
    return parseInt(sum * BigInt(x))
};