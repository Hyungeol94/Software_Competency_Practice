//https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
//LeetCode 1261. Find Elements in a Contaminated Binary Tree

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */

class FindElements {
    var root: TreeNode? 
    var cache: [Int: Bool]

    init(_ root: TreeNode?) {
        self.root = root
        self.cache = [:]
        initNode(root, 0)
    }

    func initNode(_ node: TreeNode?, _ n: Int) { 
        guard let node = node else { return }
        node.val = n
        if node.left != nil { 
            initNode(node.left, 2*n + 1)
        }
        if node.right != nil { 
            initNode(node.right, 2*n + 2)
        }
    }
    
    func findNode( _ root: TreeNode?,  _ target: Int) -> Bool { 
        guard let root = root else { 
            return false 
        }

        if target < root.val { 
            return false
        }

        if root.val == target { 
            return true
        }
        let left_result = findNode(root.left, target)
        let right_result = findNode(root.right, target)

        if left_result || right_result { 
            return true
        }

        return false
    }
    
    func find(_ target: Int) -> Bool {
        return findNode(self.root, target)
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * let obj = FindElements(root)
 * let ret_1: Bool = obj.find(target)
 */