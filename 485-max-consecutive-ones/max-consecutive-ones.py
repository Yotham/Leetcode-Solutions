class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        con = []
        c = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                print(i)
                c+=1
            else:
                con.append(c)
                c = 0
        con.append(c)
        return max(con)
            