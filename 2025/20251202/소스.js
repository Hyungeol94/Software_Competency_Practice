//https://leetcode.com/problems/count-number-of-trapezoids-i/?envType=daily-question&envId=2025-12-02
//3623. Count Number of Trapezoids I

/**
 * @param {number[][]} points
 * @return {number}
 */
var countTrapezoids = function(points) {
    // trapezoid => 평행사변형
    // horizontal trapezoid => x축에 평행한 평행사변형

    //y축 공유하는 점별 그룹화
    const map = new Map()
    for (const [x, y] of points) { 
        map.set(y, BigInt((map.get(y) || 0n)) + 1n)
    }

    //각 key별 점 2개 고른 경우의 수로 변경
    for (const [key, val] of map) { 
        map.set(key, BigInt(val * (val-1n) / 2n))
    }

    //postfixSum 구하기
    const postfixSum = new Map()

    let sum = 0n
    for (const [key, val] of map) { 
        sum += val
    }

    acc = 0n
    for (const [key, val] of map) { 
        acc += val
        postfixSum.set(key, sum-acc)
    }

    let count = 0n
    for (const [key, val] of map) { 
        count += val * postfixSum.get(key)
        count %= BigInt(10 ** 9 + 7)
    }
    return parseInt(count)
};