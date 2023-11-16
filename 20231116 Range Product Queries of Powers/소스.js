//2438. Range Product Queries of Powers
//https://leetcode.com/problems/range-product-queries-of-powers/

/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
const MOD = 1e9 + 7;

var calculate = (candidates, my_stack, queries) => { 
    // console.log(candidates, my_stack)
    const power = []
    for(let i =0;i<my_stack.length;i++){
        if (my_stack[i] == 0){
            power.push(candidates[i])
        }
    }
    // console.log(power)
    const answer = []
    for(let i =0;i<queries.length;i++){
        let result = 1
        const [left, right] = queries[i]        
        for(let j =left;j<=right;j++){
            result = result*power[j]
        }
        answer.push(result % MOD)
    }
    // console.log(answer)
    return answer
}

var isConditionMet = (candidates, my_stack, n) => {
    let count = 0
    for(let i = 0;i<my_stack.length;i++){
        if (my_stack[i] == 0){  
            count += candidates[i]
        }
    }
    if (count == n){ 
        return true
    }
    return false
}

var dfs = function(depth, my_stack, candidates, n, queries){
    if (depth == candidates.length){
        if (isConditionMet(candidates, my_stack, n)){
            return calculate(candidates, my_stack, queries)
        }
    }
    else{
        for(let i = 0;i<2;i++){
            my_stack.push(i)
            value = dfs(depth+1, my_stack, candidates, n, queries)
            if (value!== undefined){
                return value
            }
            my_stack.pop()
        }
    }
}

var productQueries = function(n, queries) {
    //가능한 power의 범위를 구한다 
    //가능한 조합들을 구해본다(dfs)
    //sum up to n인지 확인하는 작업을 하며 backtracking을 한다
    let i =0
    const candidates = []
    while(Math.pow(2, i)<=n){        
        candidates.push(Math.pow(2, i));
        i++;
    }

    my_stack = []
    let value = dfs(0, my_stack, candidates, n, queries)
    return value
};