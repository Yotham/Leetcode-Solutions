# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        string = ""
        while head:
            string += str(head.val)
            head = head.next
        
        if string == string[::-1]:
            return True
        return False
