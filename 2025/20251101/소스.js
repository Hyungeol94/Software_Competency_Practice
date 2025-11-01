//https://school.programmers.co.kr/learn/courses/30/lessons/43165
//타겟 넘버

function dfs(mystack, numbers, acc, target, depth) { 
    if (depth == numbers.length) { 
        if (acc == target) { 
           return 1
        }
        return 0
    }
    
    var count = 0
    for (const i of [true, false]) { 
        mystack.push(i == true ? numbers[depth] : -numbers[depth])
        count += dfs(
            mystack,
            numbers,
            i == true ? acc+numbers[depth] : acc-numbers[depth],
            target,
            depth+1,
            count
        )
        mystack.pop()
    }
    return count
}

function solution(numbers, target) {
    const acc = 0
    const mystack = []
    const res = dfs(mystack, numbers, acc, target, 0)
    return res
}