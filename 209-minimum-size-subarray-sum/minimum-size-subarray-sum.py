class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        left = 0
        ans = 2**31
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                total-= nums[left]
                ans = min(ans,(right-left)+1)
                left+=1
        if ans == 2**31:
            return 0
        else:
            return ans

            
    

        