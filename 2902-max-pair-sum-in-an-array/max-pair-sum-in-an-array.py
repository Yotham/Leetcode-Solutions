class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = -9999

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                max1 = -9999
                for item in str(nums[i]):
                    max1 = max(max1,int(item))
                max2 = -9999
                for item in str(nums[j]):
                    max2 = max(max2,int(item))
                if max1 == max2 and max1 != -9999:
                    maxSum = max(maxSum,nums[i]+nums[j])
                    
        if maxSum == -9999:
            return -1
        return maxSum