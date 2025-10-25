//https://leetcode.com/problems/calculate-money-in-leetcode-bank/?envType=daily-question&envId=2025-10-25
//1716. Calculate Money in Leetcode Bank

/**
 * @param {number} n
 * @return {number}
 */
var totalMoney = function(n) {
    var sum = 0
    for (j = 1; j <= 7; j++ ){ 
        sum += j
    }
    var quotient = Math.floor(n / 7)
    var remainder = n % 7
    var total = quotient * sum

    var k = (quotient) * (quotient-1) / 2
    total += k * 7
    total += (remainder + 1) * (remainder) / 2 + quotient * remainder

    return total
};