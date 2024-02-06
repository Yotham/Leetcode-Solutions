class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i in range(len(nums)):
            val = target-nums[i]
            if val in hashMap:
                return [hashMap[val],i]
            hashMap[nums[i]] = i

        
            

            
