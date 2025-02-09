//https://leetcode.com/problems/count-number-of-bad-pairs/?envType=daily-question&envId=2025-02-09
//2364. Count Number of Bad Pairs

class Solution {
    func countBadPairs(_ nums: [Int]) -> Int {
        var arr: [Int] = []
        for (i, num) in nums.enumerated() { 
            arr.append(num-i)
        }
        var freqDist: [Int: Int] = [:]
        for num in arr {
            freqDist[num, default: 0] += 1
        }
        var count = 0
        for (key, value) in freqDist { 
            if 2 <= value { 
                count += (value)*(value-1) / 2 
            }
        }

        return (nums.count) * (nums.count-1) / 2 - count 
    }
}