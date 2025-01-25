// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/?envType=daily-question&envId=2025-01-25
// Make Lexicographically Smallest Array by Swapping Elements

class Solution {
    func lexicographicallySmallestArray(_ nums: [Int], _ limit: Int) -> [Int] {
        //init freqDist
        var freqDist: [Int: Int] = [:]
        for num in nums { 
            freqDist[num, default: 0] += 1
        }

        var groupedList: [Int: Array<Int>] = [:]
        var numGroup: [Int: Int] = [:]
        var prev = 0
        var group = 1
        for (key, val) in freqDist.sorted {$0.key < $1.key} { 
            if limit < key-prev { 
                group += 1
            }
            numGroup[key] = group
            for _ in 0..<val {
                groupedList[group, default: []].append(key)
            }
            prev = key
        }

        var answer: [Int] = []
        for num in nums { 
            let group = numGroup[num, default: 0]
            let curr = groupedList[group, default: []].removeFirst() 
            answer.append(curr)
        }

        return answer
    }
}