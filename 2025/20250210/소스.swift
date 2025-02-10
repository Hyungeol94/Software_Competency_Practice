//https://leetcode.com/problems/clear-digits/?envType=daily-question&envId=2025-02-10
//3174. Clear Digits

class Solution {
    func clearDigits(_ s: String) -> String {
        var count = 0 
        var temp: [Character] = []
        for c in Array(s).reversed() { 
            if c.isNumber { 
                count += 1
                continue
            }
            if 1 <= count { 
                count -= 1
                continue
            }
            temp.append(c)
        }
        return String(temp.reversed())
    }
}