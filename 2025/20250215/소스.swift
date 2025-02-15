//https://leetcode.com/problems/find-the-punishment-number-of-an-integer/
//2698. Find the Punishment Number of an Integer

struct Cache: Hashable {
    var num: Int
    var target: Int
}

class Solution {
    func dp(_ num: Int, _ target: Int, _ cacheMap: inout [Cache: Bool]) -> Bool {
        if let cache = cacheMap[Cache(num: num, target: target)] {
            return cache
        }
        var ans = false
        let numArr = Array(String(num))
        if numArr.count < 2 {
            if num == target {
                cacheMap[Cache(num: num, target: target)] = true
                return true
            }
            cacheMap[Cache(num: num, target: target)] = false
            return false
        }
        
        if num == target {
            cacheMap[Cache(num: num, target: target)] = true
            return true
        }
        
        for i in 1..<numArr.count {
            let leftArr = numArr[0..<i]
            let left = Int(String(Array(leftArr))) ?? 0
            let rightArr = numArr[i..<numArr.count]
            let right = Int(String(Array(rightArr))) ?? 0
            let res = dp(right, target-left, &cacheMap)
            if res == true {
                ans = true
                break
            }
        }

        cacheMap[Cache(num: num, target: target)] = ans
        return ans
    }

    func isConditionMet(_ n: Int, _ cacheMap: inout [Cache: Bool]) -> Bool {
        // i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
        // ex. 1, 9, 10, 36
        let num = n * n
        return dp(num, n, &cacheMap)
    }

    func punishmentNumber(_ n: Int) -> Int {
        var cacheMap: [Cache: Bool] = [:]
        var ans = 0
        for num in 1...n {
            if isConditionMet(num, &cacheMap) {
                ans += num * num
            }
        }
        return ans
    }
}