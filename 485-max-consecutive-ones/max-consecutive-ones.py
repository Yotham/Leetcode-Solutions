class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        maxC = -1
        for num in nums:
            if num == 1:
                c+=1
            else:
                if c > maxC:
                    maxC = c
                c = 0
        if c > maxC:
            return c
        return maxC
            