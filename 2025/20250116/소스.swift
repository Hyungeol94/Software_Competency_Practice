class Solution {
    func xorAllNums(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var acc = 0
        if nums2.count % 2 == 1 {
            for num in nums1 { 
                acc = acc ^ num
            }
        }
        
        if nums1.count % 2 == 1 {
            for num in nums2 { 
                acc = acc ^ num
            }
        }
        return acc
    }
}