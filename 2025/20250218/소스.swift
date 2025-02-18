//https://leetcode.com/problems/construct-smallest-number-from-di-string/description/
//2375. Construct Smallest Number From DI String

class Solution {
    func dfs(_ pattern: [Character], _ mystack: inout [Int], _ seen: inout Set<Int>) -> Bool { 
        if mystack.count == pattern.count+1 { 
            return true
        }

        guard let currNum = mystack.last else {return false}
        let currPattern = pattern[mystack.count-1]

        if currPattern == "I" { 
            if currNum+1 <= 9 { 
                for i in Array(currNum+1...9){ 
                    let nextNum = i
                    if seen.contains(nextNum){
                        continue
                    }
                    seen.insert(nextNum)
                    mystack.append(nextNum)
                    if dfs(pattern, &mystack, &seen) == true {
                        return true
                    }
                    mystack.removeLast()
                    seen.remove(nextNum)
                }
            } 
        } else { //decreasing
            if 1 <= currNum-1 {
                for i in Array(1...currNum-1) {
                    let nextNum = i
                    if seen.contains(nextNum) { 
                        continue
                    }
                    seen.insert(nextNum)
                    mystack.append(nextNum)
                    if dfs(pattern, &mystack, &seen) == true {
                        return true
                    }
                    mystack.removeLast()
                    seen.remove(nextNum)
                }
            }
        }
        return false
    }

    func smallestNumber(_ pattern: String) -> String {
        var mystack: [Int] = []
        var seen: Set<Int> = Set()
        for i in Array(1...9) { 
            mystack.append(i)
            seen.insert(i)
            if dfs(Array(pattern), &mystack, &seen) == true { 
                return mystack.map{String($0)}.joined(separator: "")
            }
            mystack.removeLast()
            seen.remove(i)
        }

        return ""
    }
}