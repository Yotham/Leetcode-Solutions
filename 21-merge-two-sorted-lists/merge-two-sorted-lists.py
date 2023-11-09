# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1 = []
        l2 = []

        while list1:
            l1.append(list1.val)
            list1 = list1.next
        while list2:
            l2.append(list2.val)
            list2 = list2.next

        if len(l1) == 0 and len(l2) == 0:
            return None
        ret = None


        fList = list(sorted(l1+l2))
        i = 0
        ret = ListNode()
        first = ret
        ret.next = ListNode()
        ret = ret.next
        for i in range(len(fList)):
            ret.val = fList[i]
            if i != len(fList)-1:
                ret.next = ListNode()
            
            ret = ret.next

        return first.next
        
            
                
                