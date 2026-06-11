# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        def helper(node):
            if not node: return None
            left = helper(node.left)
            if left:
                return left
            self.counter+=1
            if self.counter == k:
                return node.val
            right = helper(node.right)
            if right:
                return right
        return helper(root)
