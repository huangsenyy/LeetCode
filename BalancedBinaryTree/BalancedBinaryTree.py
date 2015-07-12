# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        return False if(self.calHeight(root) == -1) else True
        
    def calHeight(self, node):
        if node is None:
            return 0

        left_height = 0
        right_height = 0
        left_height += self.calHeight(node.left) 
        right_height += self.calHeight(node.right)
        
        if abs(left_height-right_height) > 1 or left_height == -1 or right_height == -1:
            return -1
        return max(left_height, right_height) + 1    
        
