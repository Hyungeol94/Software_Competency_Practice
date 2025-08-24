//https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=daily-question&envId=2025-08-24
//1493. Longest Subarray of 1's After Deleting One Element

class Solution {
    func longestSubarray(_ nums: [Int]) -> Int {
        var right = 0
        var left = 0
        let n = nums.count
        
        var maxCount = 0
        var count = 0
        var zeroCount = 0

        while right < n { 
            if nums[right] == 1 { 
                count += 1
            } else {
                zeroCount += 1
                while zeroCount > 1 { 
                    if nums[left] == 0 { 
                        zeroCount -= 1
                    } else { 
                        count -= 1
                    }
                    left += 1
                }
            }
            maxCount = max(maxCount, count)
            right += 1
        }
        return zeroCount == 1 ? maxCount : maxCount - 1
    }
}