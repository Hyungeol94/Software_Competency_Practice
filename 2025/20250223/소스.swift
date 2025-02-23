//https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
//889. Construct Binary Tree from Preorder and Postorder Traversal

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


class Solution {
    func constructFromPrePost(_ preorder: [Int], _ postorder: [Int]) -> TreeNode? {
        //root는 preorder의 첫번째 부분
        //left children까지는 알 수 있음
        if preorder.isEmpty {
            return nil
        }

        var root = TreeNode(preorder[0])
        if preorder.count == 1 {
            return TreeNode(preorder[0])
        }
        
        var i = 1
        var j = 0
        while j < postorder.count {
            if postorder[j] == preorder[1] {
                break
            }
            i += 1
            j += 1
        }

        let leftRoot = constructFromPrePost(Array(preorder[1...i]), Array(postorder[0...j]))
        let rightRoot = constructFromPrePost(Array(preorder[i+1..<preorder.count]), Array(postorder[j+1..<postorder.count-1]))
        root.left = leftRoot
        root.right = rightRoot
        return root
    }
}


let instance = Solution()
print(instance.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1]))
