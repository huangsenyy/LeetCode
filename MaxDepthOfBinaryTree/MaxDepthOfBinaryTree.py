# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        """
        @Note:
            递归计算
            root为None的情况要考虑到    
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        max_left = max_right = 0
        if root.left is not None:
            max_left = 1 + self.maxDepth(root.left)
        if root.right is not None:
            max_right = 1 + self.maxDepth(root.right)
        if max_left >= max_right:
            return max_left
        else:
            return max_right
        
        
