//1028. Recover a Tree From Preorder Traversal
//https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/

 public class TreeNode {
      public var val: Int
      public var left: TreeNode?
      public var right: TreeNode?
      public init() { self.val = 0; self.left = nil; self.right = nil; }
      public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
      public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
          self.val = val
          self.left = left
          self.right = right
      }
  }

typealias Depth = Int
class Solution {
    func recoverFromPreorder(_ traversal: String) -> TreeNode? {
        if traversal.count == 0 {
            return nil
        }
        
        let arr = Array(traversal)
        var treeMap: [Depth: TreeNode] = [:]
        
        var i = 0
        var j = i
        while (j+1 <= arr.count-1 && arr[j+1].isNumber) {
            j += 1
        }
        let str = String(arr[i...j])
        let root = TreeNode(Int(str) ?? 0)
        i = j
        var count = 0
        
        while i != arr.count-1 {
            i += 1
            let c = arr[i]
            if c == "-" {
                count += 1
            } else {
                var j = i
                while (j+1 <= arr.count-1 && arr[j+1].isNumber) {
                    j += 1
                }
                let str = String(arr[i...j])
                var prev = treeMap[count-1, default: root]
                let curr = TreeNode(Int(String(str)) ?? 0)
                treeMap[count] = curr
                if prev.left == nil {
                    prev.left = curr
                } else {
                    prev.right = curr
                    if count-1 != 0 {
                        treeMap.removeValue(forKey: count-1)
                    }
                }
                count = 0
                i = j
            }
        }
        
        return root
    }
}