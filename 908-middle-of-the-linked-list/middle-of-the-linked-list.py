# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        front = head
        i = 0
        while head:
            i+=1
            head = head.next
        head = front
        j = 0

        while head:
            if j == i//2:
                break
            j+=1
            head=head.next
        return head