# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.counter = 0
        def helper(node):
            if not node: return 
            helper(node.left)
            self.counter+=1
            if self.counter == k:
                self.res = node.val
            helper(node.right)
        helper(root)
        return self.res