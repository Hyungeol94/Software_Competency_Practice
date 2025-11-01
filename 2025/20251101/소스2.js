//https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/?envType=daily-question&envId=2025-11-01
//3217. Delete Nodes From Linked List Present in Array

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number[]} nums
 * @param {ListNode} head
 * @return {ListNode}
 */
var binarySearch = (nums, target) => { 
    var left = 0
    var right = nums.length-1
    while (left <= right) { 
        const mid = Math.floor((left + right) / 2)
        if (nums[mid] == target) { 
            return mid
        }
        if (nums[mid] > target) { 
            right = mid-1
        } else { 
            left = mid+1
        }
    }
    return left
}

var modifiedList = function(nums, head) {
    var prev = null
    var curr = head
    var sortedNums = [...nums].sort((a, b) => a - b)

    while (curr != null)  {
        index = binarySearch(sortedNums, curr.val)
        if (index < sortedNums.length && sortedNums[index] == curr.val) { // 존재함
            if (prev) {
                prev.next = curr.next    
            } else {
                head = curr.next
            }
        } else { 
            prev = curr
        }
        curr = curr.next
    }
    return head
};