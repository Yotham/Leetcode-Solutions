# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkLeftDFS(self,root,nums,left):
        if root is not None:
            if left and root.left == None and root.right == None:
                nums.append(root.val)
            self.checkLeftDFS(root.left,nums,True)
            self.checkLeftDFS(root.right,nums,False)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
        self.checkLeftDFS(root,nums,False)
        return sum(nums)

        