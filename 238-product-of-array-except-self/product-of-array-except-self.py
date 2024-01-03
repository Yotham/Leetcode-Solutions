class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_product = 1
        zero_count = nums.count(0)

        # If there are more than one 0, all products will be 0
        if zero_count > 1:
            return [0] * len(nums)

        # Compute the product of all non-zero elements
        for num in nums:
            if num != 0:
                total_product *= num

        # Generate the result array
        result = []
        for num in nums:
            if zero_count == 0:  # No zeros in the original array
                result.append(total_product // num)
            elif num == 0:       # This element is the only zero in the array
                result.append(total_product)
            else:                # This element is non-zero, but there is a zero in the array
                result.append(0)

        return result