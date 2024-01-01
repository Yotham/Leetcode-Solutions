class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        out = 0
        for stone in stones:
            if stone in jewels:
                out+=1

        return out