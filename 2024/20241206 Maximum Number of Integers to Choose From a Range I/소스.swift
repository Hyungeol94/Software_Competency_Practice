class Solution {
    func maxCount(_ banned: [Int], _ n: Int, _ maxSum: Int) -> Int {
        var acc = 0
        // 중복 제거 및 최적화를 위한 재정렬
        let sortedBanned = Array(Set(banned)).sorted {$0 < $1}
        var i = 0
        var count = 0

        for (_, num) in Array(1...n).enumerated() {
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