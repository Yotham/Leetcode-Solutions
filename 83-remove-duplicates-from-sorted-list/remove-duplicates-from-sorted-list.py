# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = []
        rturn = ListNode()
        if head == None:
            return None
        rturn.val = head.val
        start = rturn
        s.append(head.val)
        while(head != None):
            if head.val not in s:
                s.append(head.val)
                rturn.next = ListNode()
                rturn = rturn.next
                rturn.val = head.val
            head = head.next
        return start