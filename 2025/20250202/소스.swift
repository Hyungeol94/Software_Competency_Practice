//https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
//1752. Check if Array Is Sorted and Rotated

class Solution {
    func check(_ nums: [Int]) -> Bool {
        for (i, num) in nums.enumerated() { 
            var isConditionMet = true
            var prev = Int.min
            for j in i..<i+nums.count { 
                if prev <= nums[j % nums.count] { 
                    prev = nums[j % nums.count]
                } else {
                    isConditionMet = false
                }
            }
            if isConditionMet {
                return true
            }
        }
        return false
    }
}