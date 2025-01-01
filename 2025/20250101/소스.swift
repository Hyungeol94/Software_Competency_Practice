class Solution {
    func maxScore(_ s: String) -> Int {
        var accCountZeros = Array(repeating: 0, count: s.count)
        var accCountOnes = Array(repeating: 0, count: s.count)

        var acc = 0
        for (i, num_char) in Array(s).enumerated() { 
            if num_char == "0" {
                acc += 1
            }
            accCountZeros[i] = acc
        }

        acc = 0
        for (i, num_char) in Array(s).enumerated().reversed() { 
            if num_char == "1" { 
                acc += 1
            }
            accCountOnes[i] = acc
        }

        var maxVal = 0
        //non-empty 제약조건 맞추기 위한 edge case
        if s.count == 2 { 
            return accCountZeros[0] + accCountOnes[1]
        }

        for i in 1..<max(2, s.count-1) { 
            maxVal = max(maxVal, accCountZeros[i]+accCountOnes[i])
        }

        return maxVal
    }
}