class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [num for num in nums if nums.count(num) == 1]
        return a[0]