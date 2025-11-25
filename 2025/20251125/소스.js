//https://leetcode.com/problems/smallest-integer-divisible-by-k/?envType=daily-question&envId=2025-11-25
//1015. Smallest Integer Divisible by K

/**
 * @param {number} k
 * @return {number}
 */
var smallestRepunitDivByK = function(k) {
    const ends = []
    let temp = String(k)
    while (!ends.includes(temp[temp.length-1])) { 
        ends.push(temp[temp.length-1])
        temp = String(parseInt(temp) + k)
    }
    if (!ends.includes('1')) {
        return -1
    }
    
    let n = 1n
    while (true) { 
        if (n % BigInt(k) == 0) { 
            return String(n).length
        } 
        n = n*10n+1n
    }
};