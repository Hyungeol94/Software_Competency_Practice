//https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
//1749. Maximum Absolute Sum of Any Subarray

class Solution {
    func maxAbsoluteSum(_ nums: [Int]) -> Int {
        //구간의 sum을 구하는 법 accSum(right) - accSum(left)
        //그 위치에서 가장 최대일 수 있는 것은 ? 
        //음수일 경우 -> 양수를 빼야 함 max값을 빼야 함
        //양수일 경우 -> 음수를 빼야 함 min값을 빼야 함

        var acc = 0
        var accSum: [Int] = []
        for num in nums { 
            acc += num
            accSum.append(acc)
        }


        var maxVal = -10001
        var minVal = 10001
        var ans = 0
        for num in accSum { 
            maxVal = max(num, maxVal)
            minVal = min(num, minVal)
            ans = max(ans, abs(num))
            if 0 <= num {
                ans = max(ans, abs(num-minVal))
            } else { 
                ans = max(ans, abs(num-maxVal))
            }
        }

        return ans
    }
}