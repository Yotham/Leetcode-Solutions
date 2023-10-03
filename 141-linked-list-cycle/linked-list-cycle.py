# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        links = []
        while head:
            if head.next not in links:
                links.append(head.next)
            else:
                return True
            head = head.next

        return False

        