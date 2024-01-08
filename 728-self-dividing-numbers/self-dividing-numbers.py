class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        r = []
        for i in range(left,right+1):
            temp = str(i)
            check = True
            for c in temp:
                try:
                    if i % int(c) != 0:
                        check = False
                        break
                except:
                    check = False
                    break
            if check:
                r.append(i)
        return r
            
