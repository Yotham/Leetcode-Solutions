class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr) == 1:
            return [-1]
        rightMax = -1
        for i in range(len(arr)-1,-1,-1):
            newMax = max(arr[i],rightMax)
            arr[i] = rightMax
            rightMax = newMax
        return arr