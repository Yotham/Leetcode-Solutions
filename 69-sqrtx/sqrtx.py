class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = sqrt(x)
        x = floor(x)
        return int(x)