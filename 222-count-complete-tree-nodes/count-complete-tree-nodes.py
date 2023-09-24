# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def right(root):
    vals = []
    while(root != None):
        vals.append(root.val)
        if root.left != None:
            vals += left(root.left)
        root = root.right
    return vals

def left(root):
    vals = []
    while(root != None):
        vals.append(root.val)
        if root.right != None:
            vals += right(root.right)
        root = root.left
    return vals
        
    
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        totalLen = 1
        r = root.right
        l = root.left
        totalLen += (len(left(l)+right(r)))
        return totalLen
        