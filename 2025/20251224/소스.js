//https://leetcode.com/problems/apple-redistribution-into-boxes/?envType=daily-question&envId=2025-12-24
//3074. Apple Redistribution into Boxes

/**
 * @param {number[]} apple
 * @param {number[]} capacity
 * @return {number}
 */
var minimumBoxes = function(apple, capacity) {
    const sum = apple.reduce((a, b)=> (a + b))
    const arr = [...capacity].sort((a, b) => b - a)
    
    let acc = 0
    let count = 0
    console.log(sum, arr)
    for (const [i, num] of arr.entries()) { 
        count += 1
        acc += num
        if (acc >= sum) { 
            break
        }
    }

    return count
};