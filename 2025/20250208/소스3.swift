//https://leetcode.com/problems/search-in-rotated-sorted-array/description/
//33. Search in Rotated Sorted Array

class Solution {
    func binarySearch(_ nums: [Int], _ left: Int, _ right: Int, _ target: Int) -> Int {
        if left > right {
            return -1
        }
        let middle = (left + right) / 2
        if nums[middle] == target {
            return middle
        } else if target < nums[middle] {
            return self.binarySearch(nums, left, middle-1, target)
        } else {
            return self.binarySearch(nums, middle+1, right, target)
        }
    }
    
    func isSorted(_ nums: [Int], _ left: Int, _ right: Int) -> Bool {
        if nums[left] <= nums[right] {
            return true
        }
        return false
    }


    func search(_ nums: [Int], _ target: Int) -> Int {
        var left = 0
        var right = nums.count-1
        if isSorted(nums, left, right) {
            return self.binarySearch(nums, left, right, target)
        }

        while true {
            let middle = (left + right) / 2
            if isSorted(nums, 0, middle) && isSorted(nums, middle+1, nums.count-1) {
                let res1 = self.binarySearch(nums, 0, middle, target)
                let res2 = self.binarySearch(nums, middle+1, nums.count-1, target)
                if res1 != -1 {
                    return res1
                }
                if res2 != -1 {
                    return res2
                }
                return -1
            } else if nums[left] > nums[middle] {
                right = middle
                continue
            } else {
                left = middle+1
                continue
            }
        }
    }
}
