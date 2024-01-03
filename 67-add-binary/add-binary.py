class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = 0
        pwr = 0
        num2 = 0
        pwr2 = 0
        for num in reversed(a):
            num1 += int(num)*(2**pwr)
            pwr+=1
        for num in reversed(b):
            num2+= int(num)*(2**pwr2)
            pwr2+=1
        total = num1+num2
        out = ""
        pwr = 0
        if total == 0:
            return '0'
        while total > 0:
            out += str(total%2)
            total = total // 2
        return out[::-1]
            
        
