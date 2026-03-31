//https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=javascript
//폰켓몬

function solution(nums) {
    const map = new Map()
    for (const num of nums) { 
        map.set(num, (map.get(num) ?? 0) + 1)
    }
    
    const targetCount = Math.floor(nums.length / 2)
    return Math.min(targetCount, map.size)
}