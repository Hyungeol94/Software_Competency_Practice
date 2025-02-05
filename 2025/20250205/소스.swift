//1790. Check if One String Swap Can Make Strings Equal
//https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution {
    func areAlmostEqual(_ s1: String, _ s2: String) -> Bool {
        var count = 0
        let s1Arr = Array(s1)
        let s2Arr = Array(s2)
        var s1FreqDist: [Character: Int] = [:]
        var s2FreqDist: [Character: Int] = [:]

        for (c1, c2) in zip(s1Arr, s2Arr) { 
            if c1 != c2 { 
                count += 1
            }
            if 2 < count {
                break
            } 
            s1FreqDist[c1, default: 0] += 1
            s2FreqDist[c2, default: 0] += 1
        }

        for (key, val) in s1FreqDist { 
            if s2FreqDist[key, default: 0] != val { 
                return false
            }
        }

        if count == 2 || count == 0 {
            return true
        }
        return false
    }
}