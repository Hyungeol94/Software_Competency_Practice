//https://school.programmers.co.kr/learn/courses/30/lessons/12953?language=javascript
//N개의 최소공배수

function solution(arr) {
    //소수 구하기 => 에라스토스테네스의 체
    const prime_nums = []   
    const visited = Array(101).fill(false)
    for (i = 2; i <= 100; i++) { 
        if (!visited[i]) { 
            prime_nums.push(i)
            var j = 1
            while (j <= 100) { 
                const num = j*i
                visited[num] = true
                j += 1
            }
        }
    }
    
    const map = new Map()
    for (const num of arr) { 
      // 소인수분해 비슷한 것 하기
        for (const prime of prime_nums) { 
            if (prime > num) { 
                break
            } 
            var count = 0
            var i = num
            while (true) { 
                const remainder = i % prime 
                if (remainder != 0) { 
                    break
                }
                count += 1
                const quotient = i / prime
                i = quotient
            }
            map.set(prime, Math.max(map.get(prime) || 0, count))
        }
    }
    var res = 1
    for (const [key, value] of map) { 
        res *= key ** value
    }
    return res
}