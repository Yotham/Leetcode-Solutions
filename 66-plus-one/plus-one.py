class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strings = ""
        for number in digits:
            strings += str(number)
        temp = str(int(strings) +1)
        rturn = []
        for i in range(len(temp)):
            rturn.append(int(temp[i]))
        return rturn