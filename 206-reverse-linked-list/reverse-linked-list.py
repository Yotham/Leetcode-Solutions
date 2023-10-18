# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list_ = []
        front = head
        while head:
            list_.append(head.val)
            head = head.next
        list_ = list(reversed(list_))
        head = front
        index = 0
        rList = ListNode()
        if len(list_) == 0:
            return None
        front = rList
        rList.val = list_[0]
        for i in range(0,len(list_)):
            rList.val = list_[i]
            if i != len(list_)-1:
                rList.next = ListNode()
                rList = rList.next
        

        rList = front
        return rList
        