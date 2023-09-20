# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderHelper(self,root,result):
        if(root == None):
            return result
        else:
            self.inorderHelper(root.left,result)
            result.append(root.val)
            self.inorderHelper(root.right,result)
        return result
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        result = self.inorderHelper(root,result)
        return result

        