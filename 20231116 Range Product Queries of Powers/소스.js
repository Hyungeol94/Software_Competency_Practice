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
        if (my_stack[i] == 1){
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
    let sum = 0
    for(let i = 0;i<my_stack.length;i++){
        if (my_stack[i] == 0){  
            sum += candidates[i]
        }
    }
    if (sum == n){ 
        return true
    }
    return false
}

var dfs = function(value, depth, my_stack, candidates, n, queries, sum){
    
    if (depth == candidates.length){ // 이 조건이 왜  필요하지?
        if (sum == n){
            value[0] = calculate(candidates, my_stack, queries)
            return
        }
    }

    else{
        for(let i = 0;i<2;i++){
            my_stack.push(i)
            if(i == 1){
                sum += candidates[depth]
            }
            if (sum <= n){
              dfs(value, depth+1, my_stack, candidates, n, queries, sum)   
            }
            my_stack.pop()
            if(i == 1){
                sum -= candidates[depth]
            }
        }
    }
}

var getCandidates = (n) => {
  let i = 0
  const candidates = []
    while(Math.pow(2, i)<=n){        
        candidates.push(Math.pow(2, i));
        i++;
    }
  return candidates
}

var productQueries = function(n, queries) {
    //가능한 power의 범위를 구한다 
    //가능한 조합들을 구해본다(dfs)
    //sum up to n인지 확인하는 작업을 하며 backtracking을 한다
    const candidates = getCandidates(n)
    let sum = 0
    let my_stack = []
    let value = [[]]
    dfs(value, 0, my_stack, candidates, n, queries, sum)
    return value[0]
};
