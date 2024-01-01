# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,root,final):
        if root is not None:
            if root.val is not None:
                final.append(root.val)
            self.dfs(root.left,final)
            self.dfs(root.right,final)


    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        final = []
        self.dfs(root,final)
        return final
        