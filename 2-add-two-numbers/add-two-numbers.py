# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1Nums = []
        l2Nums = []

        while(l1 != None):
            l1Nums.append(str(l1.val))
            l1 = l1.next

        while(l2 != None):
            l2Nums.append(str(l2.val))
            l2 = l2.next
        strNum1 = "".join(reversed(l1Nums))
        strNum2 = "".join(reversed(l2Nums))
        total = str(int(strNum1) + int(strNum2))
        ret = ListNode()
        temp = ret
        print(total)
        last = ListNode()
        s = len(total)
        i = 0
        for c in reversed(total):
            ret.val = int(c)
            if i != s-1:
                ret.next = ListNode()
            ret = ret.next
            i+=1

        
        return temp