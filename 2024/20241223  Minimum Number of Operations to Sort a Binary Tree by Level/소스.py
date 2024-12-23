from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count_swap(self, node_arr1, node_arr2):
        count = 0
        arr1 = list(map(lambda a: a.val, node_arr1))
        arr2 = list(map(lambda a: a.val, node_arr2))
        n = len(arr1)
        index_dict = {val : i for i, val in enumerate(arr1)}
        for i in range(n):
            if arr1[i] != arr2[i]:
                j = index_dict[arr2[i]]
                arr1[i], arr1[j] = arr1[j], arr1[i]
                index_dict[arr1[i]] = i
                index_dict[arr1[j]] = j
                count += 1
        return count
                

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        myqueue = deque([root])
        curr_level = 0
        minOperations = 0
        while myqueue:
            next_level_nodes = []
            while myqueue:
                curr = myqueue.popleft()
                if curr.left:
                    next_level_nodes.append(curr.left)
                if curr.right:
                    next_level_nodes.append(curr.right)
            sorted_arr = sorted(next_level_nodes, key=lambda a: a.val)
            ##count swap
            count = self.count_swap(next_level_nodes, sorted_arr)
            minOperations += count
            myqueue = deque(next_level_nodes)

        return minOperations