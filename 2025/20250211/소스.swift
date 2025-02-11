//https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
//1910. Remove All Occurrences of a Substring

class Solution {
    func indexOfMatch(_ s: [Character], _ part: [Character], _ partialMatchTable: [Int]) -> Int {
        var index = 0
        var length = 0
        for (i, c) in s.enumerated() {
            while part[length] != c && length != 0 {
               length = partialMatchTable[length-1]
           }
            if c == part[length] {
                length += 1
            }
            if length == part.count {
                return i-part.count+1
            }
        }
        return -1
    }


    func removeOccurrences(_ s: String, _ part: String) -> String {
        //KMP로 해보기
        var partialMatchTable: [Int] = []
        var length = 0
        let partArr = Array(part)
        for (i, c) in partArr.enumerated() {
            if i == 0 {
                partialMatchTable.append(length)
                continue
            }
            while partArr[length] != c && length != 0 {
                length = partialMatchTable[length-1]
            }
            if partArr[length] == c {
                length += 1
            }
            partialMatchTable.append(length)
        }
        
        print(partialMatchTable)
        //매칭 테이블 활용해서 찾기-> 지우기 반복
        var sArr = Array(s)
        while !sArr.isEmpty {
            //  print(sArr)
            let res = self.indexOfMatch(sArr, partArr, partialMatchTable)
            if res == -1 {
                break
            }
            // let newArr = Array(sArr[0..<res] + sArr[res+part.count..<sArr.count])
            sArr.removeSubrange(res..<res + partArr.count)
            sArr = newArr
        }
        return String(sArr)
    }
}