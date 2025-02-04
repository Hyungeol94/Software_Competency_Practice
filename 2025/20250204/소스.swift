//https://leetcode.com/problems/maximum-ascending-subarray-sum/
//1800. Maximum Ascending Subarray Sum

class Solution {
    func maxAscendingSum(_ nums: [Int]) -> Int {

        let n = nums.count
        var right = 0
        var maxSum = nums[right]
        var currSum = 0
        var prev = 0

        while right != n { 
            if nums[right] <= prev { 
                maxSum = max(maxSum, currSum)
                currSum = 0
            }
            currSum += nums[right]
            prev = nums[right]
            right += 1
        }
        maxSum = max(maxSum, currSum)
        return maxSum
    }
}