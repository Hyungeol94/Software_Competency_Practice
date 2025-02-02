//https://leetcode.com/problems/special-array-i/description/
//3151. Special Array I

class Solution {
    func isArraySpecial(_ nums: [Int]) -> Bool {
        let n = nums.count
        for i in 0..<n {
            if i == n-1 { 
                break
            }
        if nums[i] % 2 == nums[i+1] % 2 {
            return false
        }
        }
    return true
}
}