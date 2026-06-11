# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, minVal, maxVal):
            if not node: return True
            if node.val > minVal and node.val < maxVal:
                return isValid(node.left, minVal, node.val) and isValid(node.right, node.val, maxVal)
            return False
        return isValid(root,-1001,1001)
