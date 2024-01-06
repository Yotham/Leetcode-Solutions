class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            add = nums[nums[i]]
            if add not in ans:
                ans.append(add)
        return ans