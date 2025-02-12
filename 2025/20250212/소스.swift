//https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/
//2342. Max Sum of a Pair With Equal Sum of Digits

class Solution {
    func maximumSum(_ nums: [Int]) -> Int {
        var sumDigits: [Int: [Int]] = [:]
        
        for num in nums {
            var sum: Int = 0
            for i in Array(String(num)) { 
                sum += Int(String(i)) ?? 0
            }
            sumDigits[sum, default: []].append(num)
        }
        
        var answer = -1
        for key in sumDigits.keys { 
            sumDigits[key, default: []].sort()
            if let list = sumDigits[key], 2 <= list.count { 
                answer = max(answer, list[list.count-1] + list[list.count-2])
            }
        }

        return answer
    }
}