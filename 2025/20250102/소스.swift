// Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/description/?envType=daily-question&envId=2025-01-02

class Solution {
    func vowelStrings(_ words: [String], _ queries: [[Int]]) -> [Int] {
        var prefixSums: [Int] = []
        let vowels = ["a", "e", "i", "o", "u"]
        var acc = 0
        for word in words { 
            let arr = Array(word)
            if (vowels.contains(String(arr[0]))) && (vowels.contains(String(arr[arr.count-1]))) { 
                acc += 1
            }
            prefixSums.append(acc)
        }

        var answer: [Int] = []
        for query in queries {
            let start = query[0]
            let end = query[1]
            let startPrefix = (0 <= start - 1) ? prefixSums[start-1] : 0
            let endPrefix = prefixSums[end]
            answer.append(endPrefix - startPrefix)
        }
        return answer
    }
}