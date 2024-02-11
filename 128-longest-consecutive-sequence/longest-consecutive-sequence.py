class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        nums = set(nums)
        maxSeq = float('-inf')
        seq = 0
        for num in nums:
            if num-1 not in nums:
                seq = 1
                currentNum = num

                while currentNum + 1 in nums:
                    seq+= 1
                    currentNum+=1

                maxSeq = max(maxSeq, seq)


        return maxSeq

                



