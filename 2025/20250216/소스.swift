//https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/submissions/1544884148/
//1718. Construct the Lexicographically Largest Valid Sequence

class Solution {
    func dfs(_ arr: inout [Int], _ n: Int, _ seen: inout Set<Int>) -> Bool {
        let limit = arr.count
        var index = 0
        if seen.count == n {
            return true
        }

        for i in 0..<limit {
            if arr[i] == 0 {
                index = i
                break
            }
        }

        for i in (1...n).reversed() {
            if seen.contains(i) {
                continue
            }

            if i != 1 && limit <= index+i {
                continue
            }

            if i != 1 && arr[index+i] != 0 {
                continue
            }

            seen.insert(i)
            arr[index] = i
            if i != 1 {
                arr[index+i] = i
            }
            if dfs(&arr, n, &seen) {
                return true
            }
            arr[index] = 0
            if i != 1 {
                arr[index+i] = 0
            }
            seen.remove(i)
        }

        return false
    }

    func constructDistancedSequence(_ n: Int) -> [Int] {
        if n == 1 {
            return [1]
        }
        var arr = Array(repeating: 0, count: 1+2*(n-1))
        var seen: Set<Int> = Set()
        dfs(&arr, n, &seen)
        return arr
    }
}
