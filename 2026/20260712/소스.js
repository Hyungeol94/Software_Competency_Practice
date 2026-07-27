//https://leetcode.com/problems/rank-transform-of-an-array/submissions/2065490640/?envType=daily-question&envId=2026-07-12
//1331. Rank Transform of an Array

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    const unique_arr = [...new Set(arr)]     
    unique_arr.sort((a, b) => a-b)
    console.log(unique_arr)
    const ranks = new Map()
    for (const [i, num] of unique_arr.entries()){
        ranks.set(num, i+1)
    }                
    
    return arr.map((num) => ranks.get(num))

};