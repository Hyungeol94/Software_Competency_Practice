//https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
//2657. Find the Prefix Common Array of Two Arrays

class Solution {
    func findThePrefixCommonArray(_ A: [Int], _ B: [Int]) -> [Int] {
        var setA = Set<Int>()
        var setB = Set<Int>()
        var answer: [Int] = []
        var acc = 0
        for (a, b) in zip(A, B) { 
            setA.insert(a)
            setB.insert(b)
            let common = setA.intersection(setB)
            setA.subtract(common)
            setB.subtract(common)
            acc += common.count
            answer.append(acc)
        }
        return answer
    }
}