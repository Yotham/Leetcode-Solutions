class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        final_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in final_dict:
                return [final_dict[target - nums[i]], i]
            final_dict[nums[i]] = i
        return []


            
