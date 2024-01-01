class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        sol = 99999999999
        while True:
            if len(str(sol)) == 1:
                return sol
            sol = 0
            for c in num:
                sol+= int(c)
            num = str(sol)