class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        maxC = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c+=1
            else:
                if c > maxC:
                    maxC = c
                c = 0
        if c > maxC:
            return c
        return maxC
            