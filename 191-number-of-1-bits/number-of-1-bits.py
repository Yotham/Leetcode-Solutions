class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = '{0:08b}'.format(n)
        return n.count("1")