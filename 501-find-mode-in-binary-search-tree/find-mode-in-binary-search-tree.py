# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def dfs(self,root,l):
        if root is not None:
            l.append(root.val)
            self.dfs(root.left,l)
            self.dfs(root.right,l)
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        self.dfs(root,l)
        maxCount = 0
        for val in l:
            count = l.count(val)
            if count > maxCount:
                maxCount = count
        output = []
        add = [output.append(val) for val in l if l.count(val) == maxCount and val not in output]
        return output
            

        