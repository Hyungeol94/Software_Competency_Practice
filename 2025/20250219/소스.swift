//https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
//1415. The k-th Lexicographical String of All Happy Strings of Length n

class Solution {
    func dfs(_ n: Int, _ mystack: inout [Character], _ strings: inout [String]) {
     if mystack.count == n { 
        strings.append(String(mystack))
        return
     }

     for c in ["a", "b", "c"] as [Character] { 
        if let last = mystack.last, c == last { 
            continue
        }
        mystack.append(c)
        dfs(n, &mystack, &strings)
        mystack.removeLast()
        }
    }

    func getHappyString(_ n: Int, _ k: Int) -> String {
        var mystack: [Character] = []
        var strings: [String] = []
        dfs(n, &mystack, &strings)
        if strings.count < k { 
            return ""
        } 
        return strings[k-1]
    }
}