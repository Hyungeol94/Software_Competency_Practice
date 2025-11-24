//https://leetcode.com/problems/binary-prefix-divisible-by-5/?envType=daily-question&envId=2025-11-24
//1018. Binary Prefix Divisible By 5

/**
 * @param {number[]} nums
 * @return {boolean[]}
 */
var prefixesDivBy5 = function(nums) {
    let str = "0b"
    const answer = []
    for (const [i, num] of nums.entries()) { 
        str += num
        if (BigInt(str) % 5n == 0n) { 
            answer.push(true)
        } else { 
            answer.push(false)
        }
    }
    return answer
};