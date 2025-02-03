//https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/?envType=daily-question&envId=2025-02-03
//3105. Longest Strictly Increasing or Strictly Decreasing Subarray

class Solution {
    func longestMonotonicSubarray(_ nums: [Int]) -> Int {
        //Kadane's algorithm
        var maxLen = 1
        let n = nums.count

        //find strictly increasing subarray
        var left = 0
        var right = 1
        var prev = nums[left]
        while right != n { 
            if nums[right] <= prev {
                maxLen = max(maxLen, right-left)
                left = right
            }
            prev = nums[right]
            right += 1
        }
        maxLen = max(maxLen, right-left)

        //find strictly decreasing subarray
        left = 0
        right = 1
        prev = nums[left]
        while right != n { 
            if prev <= nums[right] { 
                maxLen = max(maxLen, right-left)
                left = right
            }
            prev = nums[right]
            right += 1
        }
        maxLen = max(maxLen, right-left)
        return maxLen
    }
}