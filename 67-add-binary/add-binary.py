class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        pow1 = len(a)-1
        pow2 = len(b)-1
        sum1 = 0
        sum2 = 0
        itr = 0
        itr2 = 0
        for x in a:
            sum1 += int(x) * pow(2,pow1)
            pow1-=1
        for x in b:
            sum2 += int(x) * pow(2,pow2)
            pow2-=1
        total = sum1+sum2
        str1 = ""
        q = total
        while(q != 0):
            r = q%2
            str1 += str(r)
            q = q/2
        str1 = str1[::-1]
        if(str1 == ""):
            return "0"
        return str1