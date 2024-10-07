class Solution {
    func tweak(_ s: String) -> String {
        var arr = Array(s)
        var i = 0
        var isFound = false
        while i < arr.count-1 {
            if arr[i] == "A" && arr[i+1] == "B" {
                isFound = true
                break
            }
            if arr[i] == "C" && arr[i+1] == "D"{
                isFound = true
                break
            }
            i += 1
        }
        if !isFound {
            return s
        }
        let leftS = String(arr[0..<i])
        let rightS = String(arr[i+2..<arr.count])
        return leftS + rightS
    }

    func minLength(_ s: String) -> Int {
        var curr = s
        while true {
            let isFound = false
            let tweakedString = tweak(curr)
            if tweakedString == curr {
                break
            }
            curr = tweakedString
        }
        return curr.count
    }
}