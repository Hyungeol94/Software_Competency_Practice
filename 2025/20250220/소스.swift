//https://leetcode.com/problems/find-unique-binary-string/submissions/
//1980. Find Unique Binary String

class Solution {
    func findDifferentBinaryString(_ nums: [String]) -> String {
        let n = nums.count
        let bound = 1 << n 
        var arr = Array(repeating: false, count: bound)
        for num in nums { 
            let decimal = Int(num, radix: 2) ?? 0
            arr[decimal] = true
        }

        for (i, bool) in arr.enumerated() { 
            if bool == false { 
                let ans = String(i, radix: 2) ?? ""
                return String(repeating: "0", count: n-ans.count)+ans
            }
        }
        return ""
    }
}