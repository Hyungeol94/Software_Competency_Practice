// https://leetcode.com/problems/next-greater-numerically-balanced-number/?envType=daily-question&envId=2025-10-24
// 2048. Next Greater Numerically Balanced Number

/**
 * @param {number} n
 * @return {number}
 */
var nextBeautifulNumber = function(n) {
    
    var i = n+1 
    while (true) { 
        var freqDist = {}

        for (const c of String(i)) { 
            freqDist[c] = (freqDist[c] || 0) + 1 
        }
        var is_found = true
        for (const [key, value] of Object.entries(freqDist)) {
            if (Number(key) != Number(value)) { 
                is_found = false
                break
            }
        }
        if (is_found) { 
           return i 
        }
        i += 1
    }
    return i 
};