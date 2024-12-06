

class Solution {
    func maxCount(_ banned: [Int], _ n: Int, _ maxSum: Int) -> Int {
         var acc = 0
        // 중복 제거 및 최적화를 위한 재정렬
        let sortedBanned = Array(Set(banned)).sorted {$0 < $1}
        var i = 0
        var count = 0

        for num in 1...n { // direct iteration
        // Instead of creating an array, iterate directly from 1 to n. This avoids memory and performance issues.
        // Array를 만들면 n=506731976와 같은 상황(test case)에서 메모리 이슈를 만듦
            if i < sortedBanned.count && num == sortedBanned[i] { 
                i += 1
                continue
            }

            acc += num
            if maxSum < acc {
                break
            }
            count += 1
        }

        return count
    }
}