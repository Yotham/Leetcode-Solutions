# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,root,low,high,s):
        if root is not None:
            if root.val >= low and root.val <= high:
                s.append(root.val)
            self.dfs(root.left,low,high,s)
            self.dfs(root.right,low,high,s)

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root is None:
            return None
        s = []
        self.dfs(root,low,high,s)
        sol = sum(s)
        return sol

        