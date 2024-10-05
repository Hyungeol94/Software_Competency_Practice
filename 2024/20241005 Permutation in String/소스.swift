https://leetcode.com/problems/permutation-in-string/description/

class Solution {
    func check(_ s1FreqDist: [Character: Int], _ s2FreqDist: [Character: Int]) -> Bool { 
        for char in Array("abcdefghijklmnopqrstuvwxyz"){
            if s1FreqDist[char] != s2FreqDist[char] {
                return false
            }
        }
        return true
    }

    func checkInclusion(_ s1: String, _ s2: String) -> Bool {
        var diff = s1.count
        var s1FreqDist: [Character: Int] = [:]
        var s2FreqDist: [Character: Int] = [:]
        let s1Arr = Array(s1)
        let s2Arr = Array(s2)

        if s2.count < s1.count { 
            return false
        }
        
        for char in Array("abcdefghijklmnopqrstuvwxyz"){
            s1FreqDist[char, default: 0] += 0
            s2FreqDist[char, default: 0] += 0
        }
        
        for i in 0..<diff {
            s1FreqDist[s1Arr[i], default: 0] += 1 
            s2FreqDist[s2Arr[i], default: 0] += 1
        }

        var left = 0
        var right = s1.count
        while true { 
            if check(s1FreqDist, s2FreqDist) {
                return true
            }
            if right == s2.count { 
                break
            }
            s2FreqDist[s2Arr[left], default: 0] -= 1
            s2FreqDist[s2Arr[right], default: 0] += 1
            left += 1
            right += 1
        }

        return false
    }
}