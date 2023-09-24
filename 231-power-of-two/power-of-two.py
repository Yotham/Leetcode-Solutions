class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        size = min(31,n)
        for i in range(size):
            num = pow(2,i)
            if num == n:
                return True
        
        return False
        