//https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
//1524. Number of Sub-arrays With Odd Sum


import Foundation

class Solution {
    func numOfSubarrays(_ arr: [Int]) -> Int {
        var acc = 0
        var arrAcc: [Int] = []
        var numOdds: [Int] = []
        var numEvens: [Int] = []
        var numOdd = 0
        var numEven = 0
        for num in arr { 
            acc += num
            arrAcc.append(acc)
            if arrAcc.last! % 2 == 0 { 
                numEven += 1
            } else { 
                numOdd += 1
            }
            numOdds.append(numOdd)
            numEvens.append(numEven)
        }
        //홀 - 짝 = 홀
        //짝 - 홀 = 홀
        //홀 - 홀 = 짝
        //짝 - 짝 = 짝
        var count = 0
        for i in 0..<arr.count { 
            let num = arrAcc[i], numEven = numEvens[i], numOdd = numOdds[i]
            if num % 2 == 0 { 
                count += numOdd
            } else { 
                count += (1+numEven)
            }
        }
        return count % (Int(pow(10.0, 9.0)) + 7)
    }
}