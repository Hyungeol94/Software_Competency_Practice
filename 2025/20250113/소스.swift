// https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/?envType=daily-question&envId=2025-01-12
// Check if a Parentheses String Can Be Valid

class Solution {
    func canBeValid(_ s: String, _ locked: String) -> Bool {
        if s.count % 2  == 1 { 
            return false
        }
        let arrS = Array(s)
        let arrL = Array(locked)

        var mystack: [Int] = []
        var unlocked: [Int] = []

        for (i, c) in arrS.enumerated() { 
            if arrL[i] == "0" { 
                unlocked.append(i)
                continue
            }

            if arrS[i] == "(" { 
                mystack.append(i)
            }

            if arrS[i] == ")" {
                if !mystack.isEmpty { 
                    mystack.removeLast()
                } else if !unlocked.isEmpty { 
                    unlocked.removeLast()
                } else {
                    return false
                }
            }
        }

        while !mystack.isEmpty && !unlocked.isEmpty && mystack[mystack.count-1] < unlocked[unlocked.count-1] {  
                mystack.removeLast()
                unlocked.removeLast()
        }

        if !mystack.isEmpty { 
            return false
        }

        return true
        
}
}